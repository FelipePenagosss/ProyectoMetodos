from flask import Flask, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def ajuste_lineal(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    xy_mean = np.mean(x * y)
    xx_mean = np.mean(x * x)
    
    m = (xy_mean - x_mean * y_mean) / (xx_mean - x_mean ** 2)
    b = y_mean - m * x_mean
    
    ajuste = m * x + b
    error = y - ajuste
    
    iteraciones = [{'iteracion': int(i), 'x': float(x[i]), 'y': float(y[i]), 'ajuste': float(ajuste[i]), 'error': float(error[i])} for i in range(n)]
    
    return m, b, ajuste, iteraciones

@app.route('/ajuste_lineal_de_curvas', methods=['POST'])
def solve_ajuste_lineal():
    data = request.json
    x = np.array(data['x'])
    y = np.array(data['y'])

    try:
        m, b, ajuste, iteraciones = ajuste_lineal(x, y)

        # Generar la gráfica
        plt.scatter(x, y, color='blue', label='Datos Originales')
        plt.plot(x, ajuste, color='red', label='Ajuste Lineal')
        plt.grid(True)
        plt.axhline(0, color="#000000")
        plt.axvline(0, color="#000000")
        plt.title("Ajuste Lineal de Curvas")
        plt.ylabel("Eje Y")
        plt.xlabel("Eje X")
        plt.legend()

        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        # Convertir la imagen a base64
        img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

        return jsonify({'Pendiente': float(m), 'Intersección': float(b), 'Iteraciones': iteraciones, 'Imagen': img_base64})
    except Exception as e:
        return jsonify({'error': f'Error durante la ejecución: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
