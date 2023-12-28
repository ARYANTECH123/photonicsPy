
from sim_setup import mzi_factory
from simphony.libraries import siepic


class displayComponent():
    def __init__(self, ID):
        self.ID: int = ID
        self.component_type: str = None
        self.num_nodes : int= None
        
        self.component : any= None

        self.nodes : list[str]= None
        self.params: list[float] = None

        self.nets = None

    def __repr__(self) -> str:
        return self.component_type + str(self.xpos, self.ypos)

    def assign_mzi(self, l1, l2):
        self.component = mzi_factory(l1, l2)

        self.num_nodes = 2

        self.component_type = "MZI-L1_L2-in_out"

        self.params = [l1, l2]

        self.nodes = ["in", "out"]

    def assign_grating(self):
        self.component = siepic.GratingCoupler()
        self.component.rename_pins("c")

        self.component_type = "GC-null-c"

        self.nodes = ["c"]
        self.num_nodes = 1


class Circuit():

    def __init__(self, sch_name) -> None:
        self.name = sch_name

        self.components = {}
        self.nets = []

        self.connections = []

    def __repr__(self) -> str:
        return "Circuit-" + str(self.name)
    
    def add_component(self, component: displayComponent):
        self.components[component.ID] = component

    def generate_nets(self):
        for i in self.components.keys:
                for pin in self.components[i].nodes:
                    self.nets.append((i, pin))
        print(self.nets)
    
    def create_connection(self, componentID1, pin1, componentID2, pin2):
        self.connections.append(((componentID1, pin1), (componentID2, pin2)))

    def solve(self):
        for connection in self.connections:
            c1 = self.components[connection[0][0]]
            c2 = self.components[connection[1][0]]
            p1 = connection[0][1]
            p2 = connection[1][1]

            c1.component[p1].connect(c2.component[p2])

    