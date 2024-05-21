import sympy as sp
from math import *
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

def NewtonRaphson(tol):
    tabla=[]
    x=sp.symbols('x')
    f=input('Digite f(x): ')
    xi=float(input('Digite el punto de inicio(dato numerico): '))
    df=sp.diff(f)
    f= sp.lambdify(x,f)
    df=sp.lambdify(x,df)
    error=1
    cont=0
    while error>tol:
        x1=xi-(f(xi)/df(xi))
        error=abs((x1-xi)/x1)
        if(error<tol):
            print('x',cont,'=',x1,'Es la raiz')
        cont+=1
        tabla.append([cont,xi,x1,error])
        xi=x1
    print(tabulate(tabla,headers=['Iteracion','Xi','Xi+1','Error']))
    a = -10
    b = 30
    n = 50
    xn = np.linspace(a, b, n)
    yn = f(xn)
    plt.plot(xn, yn)
    plt.grid(True)
    plt.axhline(0, color="#ff0000")
    plt.axvline(0, color="#ff0000")
    plt.title("Metodo Newton Raphson")
    plt.ylabel("Eje Y")
    plt.xlabel("Eje X")
    plt.plot(xi,0, 'ro')

    if (xi!= np.nan):
        plt.axvline(xi)
    plt.show()

NewtonRaphson(0.00001)
