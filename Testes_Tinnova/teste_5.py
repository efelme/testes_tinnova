# Teste 5

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
veiculos = []
contador_id = 1

def buscar_por_id(veiculo_id):
    return next((v for v in veiculos if v['id'] == veiculo_id), None)

@app.route('/veiculos', methods=['GET'])
def listar_veiculos():
    marca = request.args.get('marca')
    ano = request.args.get('ano', type=int)
    cor = request.args.get('cor')

    resultado = veiculos

    if marca:
        resultado = [v for v in resultado if v['marca'].lower() == marca.lower()]
    if ano:
        resultado = [v for v in resultado if v['ano'] == ano]
    if cor:
        resultado = [v for v in resultado if v['descricao'].lower().find(cor.lower()) != -1]

    return jsonify(resultado), 200

@app.route('/veiculos/<int:veiculo_id>', methods=['GET'])
def listar_veiculo_por_id(veiculo_id):
    veiculo = buscar_por_id(veiculo_id)
    if veiculo:
        return jsonify(veiculo)
    return jsonify({'erro': 'Veículo não encontrado'}), 404

@app.route('/veiculos', methods=['POST'])
def cadastrar_veiculo():
    global contador_id
    dados = request.get_json()
    
    veiculo = {
        'id': contador_id,
        'veiculo': dados['veiculo'],
        'marca': dados['marca'],
        'ano': dados['ano'],
        'descricao': dados.get('descricao', ''),
        'vendido': dados.get('vendido', False),
        'created': datetime.utcnow().isoformat(),
        'updated': datetime.utcnow().isoformat()
    }
    
    veiculos.append(veiculo)
    contador_id += 1
    return jsonify(veiculo), 201

@app.route('/veiculos/<int:veiculo_id>', methods=['PUT'])
def atualizar_veiculo(veiculo_id):
    dados = request.get_json()
    veiculo = buscar_por_id(veiculo_id)
    
    if not veiculo:
        return jsonify({'erro': 'Veículo não encontrado'}), 404

    veiculo.update({
        'veiculo': dados['veiculo'],
        'marca': dados['marca'],
        'ano': dados['ano'],
        'descricao': dados['descricao'],
        'vendido': dados['vendido'],
        'updated': datetime.utcnow().isoformat()
    })

    return jsonify(veiculo), 200

@app.route('/veiculos/<int:veiculo_id>', methods=['PATCH'])
def atualizar_dados_veiculo(veiculo_id):
    dados = request.get_json()
    veiculo = buscar_por_id(veiculo_id)
    
    if not veiculo:
        return jsonify({'erro': 'Veículo não encontrado'}), 404

    for campo in ['veiculo', 'marca', 'ano', 'descricao', 'vendido']:
        if campo in dados:
            veiculo[campo] = dados[campo]

    veiculo['updated'] = datetime.utcnow().isoformat()

    return jsonify(veiculo), 200

@app.route('/veiculos/<int:veiculo_id>', methods=['DELETE'])
def deletar_veiculo(veiculo_id):
    global veiculos
    veiculo = buscar_por_id(veiculo_id)
    
    if not veiculo:
        return jsonify({'erro': 'Veículo não encontrado'}), 404

    veiculos = [v for v in veiculos if v['id'] != veiculo_id]
    return jsonify({'mensagem': f'Veículo {veiculo_id} removido com sucesso.'}), 200

if __name__ == '__main__':
    app.run(debug=True)