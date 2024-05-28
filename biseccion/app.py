from flask import Flask, request, jsonify

app = Flask(__name__)

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("El teorema de Bolzano no se cumple: f(a) y f(b) deben tener signos opuestos.")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("No convergió.")

@app.route('/biseccion', methods=['POST'])
def solve_biseccion():
    data = request.json
    f_str = data['function']
    a = data['a']
    b = data['b']
    
    f = lambda x: eval(f_str)
    
    try:
        root = biseccion(f, a, b)
        return jsonify({'root': root})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
