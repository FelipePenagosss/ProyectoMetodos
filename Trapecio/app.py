from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def fx(x):
    return np.sqrt(x) * np.sin(x)

def integrar_trapecios(a, b, n):
    suma = 0
    muestras = n + 1
    h = (b - a) / n

    for i in range(1, n):
        suma += fx(a + i * h)
    total = h / 2 * (fx(a) + 2 * suma + fx(b))

    return total, muestras

def generar_grafico(a, b, muestras):
    xi = np.linspace(a, b, muestras)
    fi = fx(xi)

    muestraLinea = muestras * 10
    xk = np.linspace(a, b, muestraLinea)
    fk = fx(xk)

    plt.figure()
    plt.plot(xi, fi, 'go')
    plt.plot(xk, fk)
    plt.fill_between(xi, 0, fi, color='b')
    for j in range(muestras):
        plt.axvline(xi[j], color='w')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    img_b64 = base64.b64encode(img.getvalue()).decode('utf8')
    return img_b64

@app.route('/Trapecio', methods=['POST'])
def integrar_trapecios_endpoint():
    data = request.json
    a = data['a']
    b = data['b']
    n = data['n']

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(n, int)):
        return jsonify({'error': 'Por favor, asegúrate de que los valores de a, b sean números y n sea un entero.'}), 400

    if a >= b:
        return jsonify({'error': 'El valor de a debe ser menor que el valor de b.'}), 400

    if n <= 0:
        return jsonify({'error': 'El número de trapecios n debe ser mayor que 0.'}), 400

    resultado, muestras = integrar_trapecios(a, b, n)
    grafico = generar_grafico(a, b, muestras)

    return jsonify({'resultado': resultado, 'grafico': grafico})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
