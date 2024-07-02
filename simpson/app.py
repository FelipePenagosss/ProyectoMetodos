from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
CORS(app)

def simpson(f, a, b, n=100):
    if n % 2 == 1:
        raise ValueError("El número de subintervalos debe ser par.")
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    S = y[0] + y[-1] + 4 * sum(y[1:n:2]) + 2 * sum(y[2:n-1:2])
    return S * h / 3

@app.route('/simpson', methods=['POST'])
def solve_simpson():
    try:
        data = request.json
        if not data:
            raise ValueError("No se enviaron datos en la solicitud.")
        
        f_str = data.get('funcion')
        a = data.get('limitea')
        b = data.get('limiteb')
        n = data.get('nimagenes', 100)  
        
        if f_str is None or a is None or b is None:
            raise ValueError("Los parámetros 'funcion', 'limitea' y 'limiteb' son obligatorios.")
        
        f = lambda x: eval(f_str, {"np": np, "x": x})
        
        resultado = simpson(f, a, b, n)
        
        x = np.linspace(a, b, n+1)
        y = f(x)
        midpoints = (x[:-1] + x[1:]) / 2
        midpoints_y = f(midpoints)
   
        plt.figure()
        plt.plot(x, y, 'b', zorder=5, label='Puntos')
        plt.scatter(x, y, color='blue')
        plt.scatter(midpoints, midpoints_y, color='red', zorder=5, label='Puntos medios')
        plt.fill_between(x, 0, y, where=((x >= a) & (x <= b)), color='skyblue', alpha=0.4)
        plt.title('Método de Simpson')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()

     
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        
     
        grafica = base64.b64encode(img.getvalue()).decode('utf-8')
        
        
        resultados = []
        for i in range(len(x) - 1):
            resultados.append({'x': float(x[i]), 'y': float(y[i])})
            resultados.append({'x': float(midpoints[i]), 'y': float(midpoints_y[i])})
        resultados.append({'x': float(x[-1]), 'y': float(y[-1])})  

        return jsonify({'Raiz': resultado, 'Grafica': grafica, 'Resultados': resultados})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f"Error inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
