from flask import Flask, request, jsonify

app = Flask(__name__)

errorMin=0.00001

def secante(funcion, x0, x1, max_iter=100):
    iteraciones = []
    for i in range(max_iter):
        error=abs((x1-x0)/x1)
        if error < errorMin:
            return x1,iteraciones
        if funcion(x1) - funcion(x0) == 0:
            raise ValueError("División por cero en la fórmula de la secante.")
        x2 = x1 - funcion(x1) * (x1 - x0) / (funcion(x1) - funcion(x0))
        iteraciones.append({
            'iteracion': i + 1,
            'x0': x0,
            'x1': x1,
            'x2': x2,
            'error': error
        })
        x0, x1 = x1, x2
    raise ValueError("No encuentra la raiz.")

@app.route('/secante', methods=['POST'])
def solucion():
    data = request.json
    f_str = data['funcion']
    x0 = data['x0']
    x1 = data['x1']
    
    funcion= lambda x: eval(f_str)
    
    try:
        raiz,iteraciones = secante(funcion, x0, x1)
        return jsonify({'raiz': raiz, 'iteraciones': iteraciones})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)