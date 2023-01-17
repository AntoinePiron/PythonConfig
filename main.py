from gns3fy import Gns3Connector, Project
from tabulate import tabulate
from json import dumps
from util import Console
from constants import data
import sys


HOST = "localhost"
allConsoles = {}


def connect_to_server():
    server = Gns3Connector(url="http://localhost:3080")
    lab = Project(name="nas", connector=server)
    lab.get()
    return lab

def basic_conf():
    for key, value in allConsoles.items():
        console = value["console"]
        console.write_cmd("conf t")
        node = value["node_info"]
        ports = node.ports
        allInterfaces = [port['name'] for port in ports if 'FastEthernet' not in port['name']]
        print("Router %s has interfaces: %s"%(key, allInterfaces))
        for interface in allInterfaces:
            #check if interface is in data
            if interface in data[key]:
                console.write_cmd("int %s"%interface)
                console.write_cmd("ip address %s %s"%(data[key][interface]['ip'], data[key][interface]['mask']))
                console.write_cmd("no shutdown")
                console.write_cmd("exit")
            print("Interface %s configured"%interface)
        console.write_cmd("int loopback 0")
        console.write_cmd("ip address 10.10.10.%s 255.255.255.255"%str(int(key)%5000+1))
        console.write_cmd("exit")
        if data[key]['CE']:
            for _, neivalue in data[key]['neigbors'].items():
                console.write_cmd("ip route 0.0.0.0 0.0.0.0 %s"%neivalue['ip'])
        console.write_cmd("end")
    print("All interfaces configured")
            
def init_ospf():
    for key, value in allConsoles.items():
        console = value["console"]
        node = value["node_info"]
        ports = node.ports
        allInterfaces = [port['name'] for port in ports if 'FastEthernet' not in port['name']]
        console.write_cmd("conf t")
        console.write_cmd("router ospf %s"%(str(100+data[key]['as_number'])))
        xval = int(key)%5000+1
        console.write_cmd("router-id %s.%s.%s.%s"%(xval, xval, xval, xval))
        for interface in allInterfaces:
            if interface in data[key]:
                console.write_cmd("network %s 255.255.255.248 area %s"%(data[key][interface]['subnetwork'],data[key]['as_number']))
        console.write_cmd("network 10.10.10.%s 255.255.255.255 area %s"%(str(int(key)%5000+1),data[key]['as_number']))
        console.write_cmd("end")

def enable_all():
    for key, value in allConsoles.items():
        console = value["console"]
        console.write_cmd("")
        console.write_cmd("enable")
    

def exit_all():
    for key, value in allConsoles.items():
        console = value["console"]
        console.write_cmd("exit")

def init_MPLS():
    for key, value in allConsoles.items():
        if data[key]['CE'] : continue
        console = value["console"]
        node = value["node_info"]
        ports = node.ports
        allInterfaces = [port['name'] for port in ports if 'FastEthernet' not in port['name']]
        console.write_cmd("conf t")
        console.write_cmd("mpls ip")
        console.write_cmd("mpls label protocol ldp")
        for interface in allInterfaces:
            if interface in data[key]:
                console.write_cmd("int %s"%interface)
                console.write_cmd("mpls ip")
                console.write_cmd("exit")
        console.write_cmd("end")
        
def init_VRF():
    for key, value in allConsoles.items():
        console = value["console"]
        console.write_cmd("conf t")
        if 'vrf' in data[key].keys():
            console.write_cmd("ip routing")
            for vrfkey, vrfvalue in data[key]['vrf'].items():
                console.write_cmd("ip vrf %s"%vrfkey)
                console.write_cmd("rd %s"%vrfvalue['rd'])
                console.write_cmd("route-target both %s"%vrfvalue['rt'])
                console.write_cmd("exit")
                interface = data[key]['vrf'][vrfkey]['interface']
                console.write_cmd("int %s"%interface)
                console.write_cmd("ip vrf forwarding %s"%vrfkey)
                console.write_cmd("ip address %s %s"%(data[key][interface]['ip'], data[key][interface]['mask']))
                console.write_cmd("no shutdown")
                console.write_cmd("exit")
                port_client = list(data[key]['neigbors'].keys())[0]
                ip_client = data[key]['neigbors'][port_client]['ip']
                console.write_cmd("ip route vrf %s 10.10.10.%s 255.255.255.255 %s"%(vrfkey,str(int(port_client)%5000+1),ip_client))
        console.write_cmd("end")
                


def init_BGP():
    for key, value in allConsoles.items():
        if not data[key]['edge'] or data[key]['CE']: continue
        print(data[key])
        console = value["console"]
        console.write_cmd("conf t")
        console.write_cmd("router bgp %s"%data[key]['as_number'])
        for port in data[key]['neigbors_bgp']:
            console.write_cmd("neighbor 10.10.10.%s remote-as %s"%(str(int(port)%5000+1),data[key]['as_number']))
            console.write_cmd("neighbor 10.10.10.%s update-source loopback 0"%str(int(port)%5000+1))
            console.write_cmd("address-family vpnv4")
            console.write_cmd("neighbor 10.10.10.%s activate"%str(int(port)%5000+1))
            console.write_cmd("neighbor 10.10.10.%s next-hop-self"%str(int(port)%5000+1))
            console.write_cmd("neighbor 10.10.10.%s send-community both"%str(int(port)%5000+1))
            console.write_cmd("exit")
            for vrfkey, vrfvalue in data[key]['vrf'].items():
                console.write_cmd("address-family ipv4 vrf %s"%vrfkey)
                console.write_cmd("redistribute static")
                console.write_cmd("redistribute connected")
                console.write_cmd("exit")
        console.write_cmd("end")
            

if __name__ == "__main__":
    lab = connect_to_server()
    print("Connected to server")
    
    if(len(sys.argv) == 2 and sys.argv[1] == "first"):
        for node in lab.nodes:
            cons = Console(node.console)
            cons.write_cmd("no")
        exit(0)

    
    for node in lab.nodes:
        if 'PC' in node.name:
            continue
        print(node.name)
        allConsoles[("%s"%node.console)] = {"console" : Console(node.console), "node_info" : node}
    if len(allConsoles) < 0:
        raise Exception("No consoles found")
    print("All consoles initialized")
    enable_all()
    basic_conf()
    init_ospf()
    init_MPLS()
    init_VRF()
    init_BGP()
    exit_all()
    
