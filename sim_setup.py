import matplotlib.pyplot as plt

from simphony.libraries import siepic
from simphony.simulators import MonteCarloSweepSimulator, SweepSimulator

gc_input = siepic.GratingCoupler()

gc_output = siepic.GratingCoupler()

def mzi_factory(l1, l2):
    '''
    Mach-Zehnder Interferometer

    Resulting pins are ('in', 'out')

    Parameters - 
    l1, l2 : Path lengths in meters (Use e-6)
    
    '''
    y_splitter = siepic.YBranch()
    wg_long = siepic.Waveguide(length=l1)
    wg_short = siepic.Waveguide(length=l2)
    y_recombiner = siepic.YBranch()

    y_splitter.rename_pins("in", "wl", "ws")
    y_recombiner.rename_pins("out", "wl", "ws")

    y_splitter["ws"].connect(wg_short["pin1"])
    y_splitter["wl"].connect(wg_long["pin1"])

    y_recombiner["ws"].connect(wg_short["pin2"])
    y_recombiner["wl"].connect(wg_long["pin2"])

    return y_recombiner.circuit.to_subcircuit()


if __name__ == "__main__":

    
    mzi = mzi_factory(150e-6, 50e-6)
    
    mzi["in"].connect(gc_input["pin1"])
    gc_output["pin1"].connect(mzi["out"])
    
    
    simulator = SweepSimulator(1500e-9, 1600e-9)
    simulator.multiconnect(gc_input, gc_output)
    
    f, p = simulator.simulate()
    plt.plot(f, p)
    plt.title("MZI")
    plt.tight_layout()
    plt.show()
    
