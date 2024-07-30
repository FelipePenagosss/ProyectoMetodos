from flask import Flask, request, jsonify
from flask_cors import CORS
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import io
import base64

app = Flask(__name__)
CORS(app)
errorMin = 0.00001

def secante(funcion, x0, x1, max_iter=100):
    iteraciones = []
    for i in range(max_iter):
        error = abs((x1 - x0) / x1)
        if error < errorMin:
            return x1, iteraciones
        if funcion(x1) - funcion(x0) == 0:
            raise ValueError("División por cero en la fórmula de la secante.")
        x2 = x1 - funcion(x1) * (x1 - x0) / (funcion(x1) - funcion(x0))
        iteraciones.append({
            'iteracion': i + 1,
            'x0': round(x0, 4),
            'x1': round(x1, 4),
            'x2': round(x2, 4),
            'error': round(error, 4)
        })
        x0, x1 = x1, x2
    raise ValueError("No encuentra la raíz.")

def generar_grafica(f_str, x0, x1, raiz):
    x = sp.symbols('x')
    funcion = sp.lambdify(x, f_str)

    fig, ax = plt.subplots()
    xn = np.linspace(x0 - 2, x1 + 2, 400)
    yn = funcion(xn)
    
    ax.plot(xn, yn, label='f(x)')
    ax.axhline(0, color='red', lw=0.5)
    ax.axvline(0, color='red', lw=0.5)
    ax.plot(raiz, 0, 'ro')
    ax.axvline(raiz, color='green', linestyle='--', lw=0.5)
    
    ax.set_title("Método Secante")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend()
    ax.grid(True)
    
    # Convertir gráfica a base64
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    
    return img_base64

@app.route('/secante', methods=['POST'])
def solucion():
    data = request.json
    f_str = data['funcion']
    x0 = data['x0']
    x1 = data['x1']
    
    funcion = lambda x: eval(f_str)
    
    try:
        raiz, iteraciones = secante(funcion, x0, x1)
        img_base64 = generar_grafica(f_str, x0, x1, raiz)
        return jsonify({'Raiz': raiz, 'Iteraciones': iteraciones, 'Imagen': img_base64})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
