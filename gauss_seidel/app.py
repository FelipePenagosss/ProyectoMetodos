# gauss_seidel_service.py

from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

def gauss_seidel(matriz, vector, error_min, iteraciones_max):
    filas, columnas = matriz.shape
    x = np.zeros(filas)
    comp = np.zeros(filas)

    for k in range(iteraciones_max):
        for valorF in range(filas):
            suma = 0
            for valorC in range(columnas):
                if valorC != valorF:
                    suma += matriz[valorF, valorC] * x[valorC]
            x[valorF] = (vector[valorF] - suma) / matriz[valorF, valorF]
        
        for valorF in range(filas):
            suma = 0
            for valorC in range(columnas):
                suma += matriz[valorF, valorC] * x[valorC]
            comp[valorF] = suma
        
        error = np.abs(comp - vector)
        if all(i <= error_min for i in error):
            break

    return x, error

@app.route('/gauss-seidel', methods=['POST'])
def resolver_gauss_seidel():
    data = request.get_json()
    matriz = np.array(data['matriz'])
    vector = np.array(data['vector'])
    error_min = data['error_min']
    iteraciones_max = data['iteraciones_max']
    
    resultado, error = gauss_seidel(matriz, vector, error_min, iteraciones_max)
    
    return jsonify({'resultado': resultado.tolist(), 'error': error.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
