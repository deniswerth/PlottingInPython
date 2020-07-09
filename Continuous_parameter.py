import numpy as np
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg') #Save plots in PDF (vectorized format)
import matplotlib
#Use of LaTeX in labels
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


#Function to plot
def f(x, alpha):
    return np.exp(- alpha * x)


#x range
x = np.linspace(0, 10, 100)
#alpha range
alpha_min = .5
alpha_max = 5
alpha_number = 20
alpha = np.linspace(alpha_min, alpha_max, alpha_number)


#Initialize plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Initialize min and max value for alpha
norm = matplotlib.colors.Normalize(vmin = alpha_min, vmax = alpha_max)
#Choose a colormap
c_m = matplotlib.cm.viridis
#Initialize the colorbar
s_m = matplotlib.cm.ScalarMappable(cmap = c_m, norm = norm)
s_m.set_array([])
cb = plt.colorbar(s_m, shrink = 0.8)
#Colorbar label with position
cb.set_label("$\\alpha$", y = 1.12, rotation = 0, labelpad = -16, fontsize = 15)

#Loop on alpha values
#For each i, plot f(x) for a value of alpha
for i in range(alpha_number):
    y = f(x, alpha[i])
    ax.plot(x, y, color = s_m.to_rgba(alpha[i]))
    

#Labels
ax.set_xlabel("$x$", fontsize = 15)
ax.set_ylabel("$y = \\exp (-\\alpha x)$", fontsize = 15)
plt.show()
