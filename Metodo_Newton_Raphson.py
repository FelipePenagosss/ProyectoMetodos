import sympy as sp
from math import *

def NewtonRaphson(tol):
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
            return
        xi=x1
        cont+=1
        print('x',cont,'=',x1)

NewtonRaphson(0.00001)
            