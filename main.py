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
        console.write_cmd("ip address 10.0.0.%s 255.255.255.0"%str(int(key)%5000+1))
        console.write_cmd("exit")
        console.write_cmd("exit")
    print("All interfaces configured")
            
def init_ospf():
    for key, value in allConsoles.items():
        console = value["console"]
        node = value["node_info"]
        ports = node.ports
        allInterfaces = [port['name'] for port in ports if 'FastEthernet' not in port['name']]
        console.write_cmd("conf t")
        console.write_cmd("router ospf 100")
        xval = int(key)%5000+1
        console.write_cmd("router-id %s.%s.%s.%s"%(xval, xval, xval, xval))
        for interface in allInterfaces:
            if interface in data[key]:
                console.write_cmd("network %s 255.255.255.0 area 0"%data[key][interface]['subnetwork'])
        console.write_cmd("exit")
        console.write_cmd("exit")

def enable_all():
    for key, value in allConsoles.items():
        console = value["console"]
        console.write_cmd("")
        console.write_cmd("enable")
    

def exit_all():
    for key, value in allConsoles.items():
        console = value["console"]
        console.write_cmd("exit")


if __name__ == "__main__":
    lab = connect_to_server()
    print("Connected to server")
    
    if(len(sys.argv) == 2 and sys.argv[1] == "first"):
        for node in lab.nodes:
            cons = Console(node.console)
            cons.write_cmd("no")
        exit(0)

    for node in lab.nodes:
        allConsoles[("%s"%node.console)] = {"console" : Console(node.console), "node_info" : node}
    if len(allConsoles) < 0:
        raise Exception("No consoles found")
    print("All consoles initialized")
    enable_all()
    basic_conf()
    init_ospf()
    exit_all()
    
