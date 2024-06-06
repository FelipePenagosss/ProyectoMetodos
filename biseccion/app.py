from flask import Flask, request, jsonify

app = Flask(__name__)

def biseccion(f, a, b, error=1e-6):
    maxima_Iteracion = 100
    iteraciones = []

    for i in range(maxima_Iteracion):
        c = (a + b) / 2
        iteraciones.append({
            'iteracion': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': f(c),
            'error': abs(f(c)),
        })
        if abs(f(c)) < error or (b - a) / 2 < error:
            return c, iteraciones
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Error")

@app.route('/biseccion', methods=['POST'])
def solve_biseccion():
    data = request.json
    f_str = data['funcion']
    a = data['x0']
    b = data['x1']
    
    f = lambda x: eval(f_str)
    
    try:
        root, iteraciones = biseccion(f, a, b)
        return jsonify({'Raiz': root, 'Iteraciones': iteraciones})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)