import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from tabulate import tabulate


print("==============================\nMÉTODO DE LA SECANTE\n==============================\n")


def secante():

#Funcion inicial
 #fdx(x):
   ## fx= x**3+2*(x**2)+10*x-20
   # return fx
 x=x  
x=sp.symbols('x')
fdx=input('Digite f(x): ')
fdx= sp.lambdify(x,fdx)
xiMenos=float(input('Digite el primer punto de inicio(dato numerico): '))
xi=float(input('Digite el segundo punto de inicio(dato numerico): '))

xnuevo=0
error = 0.0001

#Parte de procedimiento
tramo = 1
tabla=[]
iteracion=-1
while (error<tramo):
    iteracion=iteracion+1
    xnuevo = xi-(fdx(xi) * (xi - xiMenos)) / (fdx(xi) - fdx(xiMenos))
    tramo  = abs(xnuevo-xi)
    xiMenos = xi
    xi = xnuevo
    tabla.append([iteracion,xi,tramo])

# Parte de la salida
print(tabulate(tabla, headers=['Iteración','Xi','Xi+1 - Xi']))
print("========================================\nLa raíz exacta es: ", xnuevo,"\n========================================\n")
# Parte grafica
a = -2
b = 5
n = 50
xn = np.linspace(a, b, n)
yn = fdx(xn)
plt.plot(xn, yn)
plt.grid(True)
plt.axhline(0, color="#ff0000")
plt.axvline(0, color="#ff0000")
plt.title("Metodo Secante")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.plot(xi,0, 'ro')

if (xnuevo!= np.nan):
    plt.axvline(xi)#Línea vertical donde cruzan la función idéntica y el g(x)
plt.show()

secante