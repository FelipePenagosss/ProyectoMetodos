from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)  # Corregido el nombre del módulo

def jacobi_method(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    x1 = np.copy(x)
    k = 1
    error_norm = []
    while k <= max_iter:
        for i in range(n):
            summation = 0
            for j in range(n):
                if i != j:
                    summation += A[i][j] * x1[j]
            x[i] = (b[i] - summation) / A[i][i]
        error_norm.append(np.linalg.norm(x - x1))
        if error_norm[-1] < tol:
            return x.tolist(), error_norm
        x1 = np.copy(x)
        k += 1
    raise ValueError("No convergió.")

@app.route('/jacobi', methods=['POST'])
def solve_jacobi():
    data = request.json
    A = np.array(data['A'])
    b = np.array(data['b'])

    try:
        solution, error_norm = jacobi_method(A, b)
        return jsonify({'solution': solution, 'error_norm': error_norm})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':  # Corregido el nombre de _main_
    app.run(host='0.0.0.0', port=5004)
