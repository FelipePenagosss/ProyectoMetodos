from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def gauss_seidel(matriz, vector, error_min, iteraciones_max):
    filas, columnas = matriz.shape
    x = np.zeros(filas)
    comp = np.zeros(filas)
    iteraciones = []  # Lista para almacenar los resultados de cada iteración

    for k in range(iteraciones_max):
        iteracion_actual = x.copy()  # Copia del estado actual de x para almacenar
        for valorF in range(filas):
            suma = 0
            for valorC in range(columnas):
                if valorC != valorF:
                    suma += matriz[valorF, valorC] * x[valorC]
            x[valorF] = (vector[valorF] - suma) / matriz[valorF, valorF]

        iteraciones.append({'iteracion': k+1, 'x': x.tolist()})  # Almacenar la iteración actual

        for valorF in range(filas):
            suma = 0
            for valorC in range(columnas):
                suma += matriz[valorF, valorC] * x[valorC]
            comp[valorF] = suma

        error = np.abs(comp - vector)
        if all(i <= error_min for i in error):
            break

    return x, error.tolist(), iteraciones

@app.route('/gauss-seidel', methods=['POST'])
def resolver_gauss_seidel():
    data = request.json
    matriz = np.array(data['matriz'])
    vector = np.array(data['vector'])
    error_min = data.get('error_min', 1e-6)
    iteraciones_max = data.get('iteraciones_max', 100)

    # Validación de que todos los elementos en la matriz y el vector sean numéricos
    if not all(is_numeric(val) for val in matriz.flatten()) or not all(is_numeric(val) for val in vector):
        return jsonify({'error': 'Por favor, asegúrate de que todos los elementos sean números.'}), 400

    resultado, error, iteraciones = gauss_seidel(matriz, vector, error_min, iteraciones_max)

    return jsonify({'resultado': resultado.tolist(), 'error': error, 'iteraciones': iteraciones})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
