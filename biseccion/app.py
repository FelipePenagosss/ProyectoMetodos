from flask import Flask, request, jsonify

app = Flask(__name__)

def biseccion(f, a, b, error=1e-6):
    maxima_Iteracion=100
   
    for _ in range(maxima_Iteracion):
        c = (a + b) / 2
        if abs(f(c)) < error or (b - a) / 2 < error:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    raise ValueError("Error")

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
