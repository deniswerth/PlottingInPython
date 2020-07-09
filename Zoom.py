import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg') #Save plots in PDF (vectorized format)
import matplotlib
#Use of LaTeX in labels
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


#Set x and y for plotting
x = np.linspace(0, 10, 1000)
y = np.cos(50*x)*np.exp(-x)


#Initialize plot
fig, ax = plt.subplots()
ax.plot(x, y)


#Make zoom
axins = ax.inset_axes([0.5, 0.6, 0.3, 0.3])
axins.plot(x, y)
x1, x2, y1, y2 = 4, 5, -0.1, 0.1
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.set_xticklabels('')
axins.set_yticklabels('')
ax.indicate_inset_zoom(axins)


#Labels
ax.set_xlabel("$x$", fontsize = 15)
ax.set_ylabel("$y = e^{-x} \cos (50x)$", fontsize = 15)
plt.show()