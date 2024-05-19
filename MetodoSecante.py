import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate


print("==============================\nMÉTODO DE LA SECANTE\n==============================\n")

#Funcion inicial
def fdx(x):
    fx= x**3+2*(x**2)+10*x-20
    return fx
xiMenos = 0
xi = 1
xnuevo=0
error = 0.0001

