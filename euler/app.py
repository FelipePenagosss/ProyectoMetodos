from flask import Flask, request, jsonify
import math
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Funcion:
    def __init__(self, funcion):
        self.funcion = lambda x, y: eval(funcion, {'x': x, 'y': y, 'math': math})

def euler(funcion, x0, x1, y, n):
    h = (x1 - x0) / n
    X = [0] * (n + 1)
    Y = [0] * (n + 1)
    X[0] = x0
    Y[0] = y

    iteraciones = []

    for i in range(n):
        f = funcion.funcion(X[i], Y[i])
        Y[i + 1] = Y[i] + (h * f)
        X[i + 1] = X[i] + h

        iteraciones.append({
            'iteracion': i + 1,
            'X': X[i + 1],
            'Y': Y[i + 1],
            'funcion_f': f
        })

    resultado = Y[n]

    return X, Y, resultado, iteraciones

@app.route('/euler', methods=['POST'])
def resolver_euler():
    try:
        data = request.json
        funcion_cadena = data['funcion']
        x0 = data['x0']
        x1 = data['x1']
        y = data['y']
        n = data['n']

        funcion = Funcion(funcion_cadena)

        X, Y, resultado, iteraciones = euler(funcion, x0, x1, y, n)

        return jsonify({'X': X, 'Y': Y, 'resultado': resultado, 'iteraciones': iteraciones})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)
