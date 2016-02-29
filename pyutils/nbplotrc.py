import matplotlib.pyplot as plt
from cycler import cycler

def init(grid=True):
    plt.rcParams['savefig.bbox'] = 'tight'

    plt.rcParams['axes.prop_cycle'] = cycler('color', [
        "#6d904f", "#013afe", "#202020", "#fc4f30", "#e5ae38",
        "#A60628", "#30a2da", "#008080", "#7A68A6", "#CF4457",
        "#188487", "#E24A33"
    ])
    if grid:
        plt.rcParams['axes.axisbelow'] = True
        plt.rcParams["axes.grid"] =  True
        plt.rcParams["grid.linestyle"] =  "--"
        plt.rcParams["grid.linewidth"] = 1.0
        plt.rcParams["grid.color"] = "#cbcbcb"

