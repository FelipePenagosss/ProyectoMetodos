from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    iteraciones = []

    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        iteraciones.append({
            'x': x,
            'f(x)': fx,
             'iteracion': i + 1,
            'df(x)': dfx,
            'error': abs(fx)
        })
        if abs(fx) < tol:
            return x, iteraciones
        if dfx == 0:
            raise ValueError("Derivada cero. No se puede continuar.")
        x = x - fx / dfx

    raise ValueError("No convergió.")

@app.route('/newton_raphson', methods=['POST'])
def solve_newton_raphson():
    data = request.json
    f_str = data['funcion']
    df_str = data['derivada']
    x0 = data['punto_inicial']

    f = lambda x: eval(f_str)
    df = lambda x: eval(df_str)

    try:
        raiz, iteraciones = newton_raphson(f, df, x0)
        return jsonify({'Raiz': raiz, 'Iteraciones': iteraciones})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
