import randomwalks as rw
import matplotlib.pyplot as plt
import numpy as np

#Paseo Aleatorio 1
rw.plot_discrete_rm(0, 2, 5, 100)
plt.show()

#Paseo Aleatorio 2
det = lambda x, t: np.sin(t/20)
var = lambda x, t: t / 100
rw.plot_discrete_rm(0, det, var, 500)
plt.show()

#Proceso de Wiener 1
rw.plot_wiener(100, 5, 365, linewidth=1)
plt.show()

#Proceso de Wiener 2
rw.plot_wiener(100, 0.5, 365, linewidth=1)
plt.show()

#Proceso Generalizado de Wiener 1
a = 2
b = 20
rw.plot_gen_wiener(0, a, b, 3, 1000, linewidth=1)
plt.show()

#Proceso Generalizado de Wiener 2
a = -1.5
b = 5
rw.plot_gen_wiener(0, a, b, 0.1, 60, linewidth=1)
plt.show()

#Proceso de Ito 1
a = lambda x, t: np.cos(x/30)
b = lambda x, t: 2*np.cos(t/30)
rw.plot_ito(100, a, b, 1, 365, linewidth=1)
plt.show()

#Proceso de Ito 2
a = lambda x, t: 2 * np.cos(t/15)
b = lambda x, t: 3
rw.plot_ito(100, a, b, 1, 365, linewidth=1)
plt.show()

#Proceso de Ito 3
a = lambda x, t: t * np.cos(x/5)
b = lambda x, t: np.cos(t/5) / max(x, 1)
rw.plot_ito(0, a, b, 0.5, start=30, end=100, iterations=50, linewidth=0.5)
plt.show()


