import numpy as np
import matplotlib.pyplot as plt

def discrete_rm(x0, det, var, end, start=0):
    t = np.arange(start, end + 1, 1)
    size = len(t)
    x = np.empty(size)
    x[0] = x0
    
    if not callable(det):
        val_det = det
        det = lambda x, t: val_det
    
    if not callable(var):
        val_var = var
        var = lambda x, t: val_var
    
    for i in range(1, size):
        epsilon = np.random.normal(0, var(x[i-1], t[i-1]), 1)
        delta_x = det(x[i-1], t[i-1]) + epsilon
        x[i] = x[i-1] + delta_x
    return t, x

def plot_discrete_rm(x0, det, var, end, start=0, iterations=15, **kwargs):
    for i in range(iterations):
        x, y = discrete_rm(x0, det, var, end, start)
        plt.plot(x, y, **kwargs)
        plt.ylabel("x")
        plt.xlabel("t")

def wiener(z0, delta_t, end, start=0):
    t = np.arange(start, end + delta_t, delta_t)
    size = len(t)
    z = np.empty(size)
    z[0] = z0
    for i in range(1, size):
        epsilon = np.random.normal(0, 1, 1)
        delta_z = epsilon * np.sqrt(delta_t)
        z[i] = z[i-1] + delta_z
    return t, z

def plot_wiener(z0, delta_t, end, start=0, iterations=15, **kwargs):
    for i in range(iterations):
        x, y = wiener(z0, delta_t, end, start)
        plt.plot(x, y, **kwargs)
        plt.ylabel("z")
        plt.xlabel("t")

def gen_wiener(x0, a, b, delta_t, end, start=0):
    t = np.arange(start, end + delta_t, delta_t)
    size = len(t)
    x = np.empty(size)
    x[0] = x0
    for i in range(1, size):
        epsilon = np.random.normal(0, 1, 1)
        delta_x = a * delta_t + b * epsilon * np.sqrt(delta_t)
        x[i] = x[i-1] + delta_x
    return t, x

def plot_gen_wiener(x0, a, b, delta_t, end, start=0, iterations=15, **kwargs):
    for i in range(iterations):
        x, y = gen_wiener(x0, a, b, delta_t, end, start)
        plt.plot(x, y, **kwargs)
        plt.ylabel("x")
        plt.xlabel("t")

def ito(x0, a, b, delta_t, end, start=0):
    t = np.arange(start, end + delta_t, delta_t)
    size = len(t)
    x = np.empty(size)
    x[0] = x0
    for i in range(1, size):
        epsilon = np.random.normal(0, 1, 1)
        delta_x = a(x[i-1], t[i-1]) * delta_t + b(x[i-1], t[i-1]) * epsilon * np.sqrt(delta_t)
        x[i] = x[i-1] + delta_x
    return t, x

def plot_ito(x0, a, b, delta_t, end, start=0, iterations=15, **kwargs):
    for i in range(iterations):
        x, y = ito(x0, a, b, delta_t, end, start)
        plt.plot(x, y, **kwargs)
        plt.ylabel("x")
        plt.xlabel("t")