import matplotlib.pyplot as plt

from simphony.libraries import siepic
from simphony.simulators import MonteCarloSweepSimulator, SweepSimulator

from ckt import displayComponent

input = displayComponent(1)
mzi = displayComponent(2)
output = displayComponent(3)

input.assign_grating()
output.assign_grating()

mzi.assign_mzi(150e-6, 50e-6)

components = {1:input, 2:mzi, 3:output}

nets = []

for i in [1, 2, 3]:
    for pin in components[i].nodes:
        nets.append((i, pin))

print(nets)


connections = [((1, 'c'), (2, 'in')),
                ((2, 'out'), (3, 'c'))]

for connection in connections:
    c1 = components[connection[0][0]]
    c2 = components[connection[1][0]]
    p1 = connection[0][1]
    p2 = connection[1][1]

    c1.component[p1].connect(c2.component[p2])

simulator = SweepSimulator(1500e-9, 1600e-9)
simulator.multiconnect(input.component, output.component)

f, p = simulator.simulate()
plt.plot(f, p)
plt.title("MZI")
plt.tight_layout()
plt.show()
