import matplotlib.pyplot as plt
from cycler import cycler

def init_plotting(grid=False):
    plt.rcParams['figure.figsize'] = (7,4)
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.labelsize'] = 'large'
    plt.rcParams['axes.titlesize'] = 'x-large'
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.markeredgewidth'] = 1.5
    plt.rcParams['patch.linewidth'] = 0.5
    plt.rcParams['legend.fontsize'] = 'medium'
    plt.rcParams['legend.frameon'] = False
    plt.rcParams['legend.loc'] = 'center left'
    plt.rcParams['legend.scatterpoints'] = 1
    plt.rcParams['xtick.labelsize'] = 'medium'
    plt.rcParams['ytick.labelsize'] = 'medium'
    plt.rcParams['xtick.major.size'] = 3
    plt.rcParams['xtick.minor.size'] = 3
    plt.rcParams['xtick.major.width'] = 1
    plt.rcParams['xtick.minor.width'] = 1
    plt.rcParams['ytick.major.size'] = 3
    plt.rcParams['ytick.minor.size'] = 3
    plt.rcParams['ytick.major.width'] = 1
    plt.rcParams['ytick.minor.width'] = 1
    plt.rcParams['savefig.bbox'] = 'tight'
    plt.rcParams['savefig.pad_inches'] = 0.1
    plt.rcParams['savefig.dpi'] = 2*plt.rcParams['savefig.dpi']
    plt.rcParams['savefig.facecolor'] = '#f0f0f0'
    plt.rcParams['savefig.edgecolor'] = '#f0f0f0'
    plt.rcParams['errorbar.capsize'] = 6
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

  # "examples.directory": "",
  # "lines.solid_capstyle": "butt",
  # "figure.subplot.left"    : 0.08,
  # "figure.subplot.right"   : 0.95, 
  # "figure.subplot.bottom"  : 0.07,
  # "figure.subplot.hspace"  : 0.5,
