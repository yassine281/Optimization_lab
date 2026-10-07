import numpy as np

def f_test(x):
    return (x - 1)**2

def f_1(x):
    return 4*x**3 - 8*x**2 - 11*x + 5

def f_2(x):
    return x + 3/(x**2) if x != 0 else np.inf

def f_3(x):
    return (x + 2.5)**4 - x**2

def f_4(x):
    return -np.sin(x) - np.sin(3*x)/3

def f_5(x):
    return -2*np.sin(x) - np.sin(2*x) - 2*np.sin(3*x)/3