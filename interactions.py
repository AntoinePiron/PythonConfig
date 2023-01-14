from constants import data
from util import Console
from gns3fy import Gns3Connector, Project
import sys


class interactions:
    allConsoles = {}
    key = None
    value = None
    console = None
    node = None

    def __init__(self, allConsoles):
        self.allConsoles = allConsoles
        self.start_interactions()

    def send_command(self, cmd):
        self.console.write_cmd("en")

    def choose_a_router(self):
        r = input("Quel routeur voulez vous modifier ?")
        print(list(data.keys()))
        while not (r in list(data.keys())):
            r = input("Ce routeur n'est pas disponible, \n routeurs = {}".format(list(data.keys())))
        print("Routeur choisi : " + r)
        key = r
        value = self.allConsoles[key]
        console = value["console"]
        node = value["node_info"]

    def start_interactions(self):
        while (True):
            r = self.choose_a_router()
            self.send_command("en")
