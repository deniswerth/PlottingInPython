[![Python](https://img.shields.io/badge/python-3.8.2-blue.svg)](https://python.org)


# PlottingInPython

This repository presents some small and comprehensible Python codes to generate plots.

- Zoom in a plot: `Zoom.py`

- Continuously vary a parameter: `Continuous_parameter.py`

Examples of plots can be found in Plots file. Note that only numpy and matplotlib are necessary to generate plots. However, one can customize the plots (for example use a LaTeX font for the labels) by using the following code lines

```python
import os
os.environ['PATH'] = os.environ['PATH'] + ':/Library/TeX/texbin/'
from matplotlib import cm
from matplotlib import rc
plt.rcParams['axes.labelsize'] = 15                                                                                                     
plt.rcParams['legend.fontsize'] = 10                                                                                                     
plt.rcParams['xtick.labelsize'] = 10                                                                                                     
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = "serif"                                                                                                   
plt.rcParams['font.serif'] = "cm"
```
