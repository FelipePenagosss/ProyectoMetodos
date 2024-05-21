import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import sympy as sp

print("==============================\nMÉTODO DE LA SECANTE\n==============================\n")

# Solicitar fdx, xiMenos y xi por consola
def solicitar_funcion():
    while True:
        try:
            funcion_str = input("Introduce la función f(x) en términos de x (por ejemplo, x**3 + 2*(x**2) + 10*x - 20):\n")
            x = sp.symbols('x')
            funcion = sp.sympify(funcion_str)
            # Comprobar si la función se puede evaluar
            funcion.evalf(subs={x: 1})
            return funcion
        except (sp.SympifyError, TypeError) as e:
            print(f"Error en la función: {e}. Por favor, inténtalo de nuevo.")

# Pide la función al usuario
x = sp.symbols('x')
funcion = solicitar_funcion()

while True:
    try:
        xiMenos = float(input("Introduce el valor de xi-1:\n"))
        break
    except ValueError:
        print("Valor no válido. Introduce un número.")

while True:
    try:
        xi = float(input("Introduce el valor de xi:\n"))
        break
    except ValueError:
        print("Valor no válido. Introduce un número.")

error = 0.0001

# Parte de procedimiento
tramo = 1
tabla = []
iteracion = -1
while error < tramo:
    iteracion += 1
    xiMenos_val = funcion.evalf(subs={x: xiMenos})
    xi_val = funcion.evalf(subs={x: xi})
    xnuevo = xi - (xi_val * (xi - xiMenos)) / (xi_val - xiMenos_val)
    tramo = abs(xnuevo - xi)
    xiMenos = xi
    xi = xnuevo
    tabla.append([iteracion, float(xi), float(tramo)])

# Parte de la salida
print(tabulate(tabla, headers=['Iteración', 'Xi', 'Xi+1 - Xi']))
print("========================================\nLa raíz exacta es: ", float(xnuevo), "\n========================================\n")

# Parte gráfica
a = -2
b = 5
n = 50
xn = np.linspace(a, b, n)
yn = [funcion.evalf(subs={x: i}) for i in xn]
plt.plot(xn, yn)
plt.grid(True)
plt.axhline(0, color="#ff0000")
plt.axvline(0, color="#ff0000")
plt.title("Método Secante")
plt.ylabel("Eje Y")
plt.xlabel("Eje X")
plt.plot(float(xi), 0, 'ro')

if not np.isnan(float(xnuevo)):
    plt.axvline(float(xnuevo))  # Línea vertical donde cruzan la función idéntica y el g(x)
plt.show()
