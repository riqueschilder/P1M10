from flask import Flask, jsonify, request
from werkzeug.urls import url_unquote

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

pedidos = []

@app.route('/novo', methods=['POST'])
def cadastrar_pedido():
    data = request.get_json()
    pedidos.append(data)
    return jsonify({'id': len(pedidos) - 1})

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    return jsonify(pedidos)

@app.route('/pedidos/<int:id>', methods=['GET'])
def get_pedido(id):
    if id < len(pedidos):
        return jsonify(pedidos[id])
    else:
        return jsonify({'message': 'Pedido não encontrado'}), 404

@app.route('/pedidos/<int:id>', methods=['PUT'])
def editar_pedido(id):
    data = request.get_json()
    if id < len(pedidos):
        pedidos[id] = data
        return jsonify({'message': 'Pedido atualizado'})
    else:
        return jsonify({'message': 'Pedido não encontrado'}), 404

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def excluir_pedido(id):
    if id < len(pedidos):
        del pedidos[id]
        return jsonify({'message': 'Pedido excluído'})
    else:
        return jsonify({'message': 'Pedido não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
