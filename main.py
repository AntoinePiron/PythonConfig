from gns3fy import Gns3Connector, Project
from tabulate import tabulate
from json import dumps

HOST = "localhost"


def connect_to_server():
    server = Gns3Connector(url="http://localhost:3080")
    lab = Project(name="nas", connector=server)
    lab.get()
    return lab


if __name__ == "__main__":
    lab = connect_to_server()
    print(lab.stats)
    for node in lab.nodes:
        print(
            f"Node: {node.name} -- Node Type: {node.node_type} -- Status: {node.status}")
        print(node.console)
