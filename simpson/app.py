from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

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
        a = data.get('a')
        b = data.get('b')
        n = data.get('n', 100)  # Número de subintervalos, por defecto 100
        
        if f_str is None or a is None or b is None:
            raise ValueError("Los parámetros 'funcion', 'a' y 'b' son obligatorios.")
        
        f = lambda x: eval(f_str, {"np": np, "x": x})
        
        result = simpson(f, a, b, n)
        return jsonify({'Resultado': result})
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f"Error inesperado: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
