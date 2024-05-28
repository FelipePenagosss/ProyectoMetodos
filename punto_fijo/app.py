from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_next = g(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    raise ValueError("No convergió.")

@app.route('/punto_fijo', methods=['POST'])
def solve_punto_fijo():
    data = request.json
    g_str = data['funcion']
    x0 = data['punto_inicial']

    # Definir la función g utilizando eval
    try:
        g = lambda x: eval(g_str, {"math": math, "x": x, "__builtins__": {}})
    except Exception as e:
        return jsonify({'error': f'Error en la función: {str(e)}'}), 400

    try:
        root = punto_fijo(g, x0)
        return jsonify({'root': root})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Error durante la ejecución: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)