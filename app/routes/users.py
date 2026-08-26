from flask import Blueprint, jsonify, request
from app.models.user import usuarios, criar_usuario

users_bp = Blueprint('users', __name__)

@users_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@users_bp.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    if not data or not data.get('nome') or not data.get('email'):
        return jsonify({'erro': 'Nome e email sao obrigatorios'}), 400

    nome = data.get('nome')
    email = data.get('email')

    novo_usuario = criar_usuario(nome, email)
    return jsonify({'data': novo_usuario}), 201

@users_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def buscar_usuario(usuario_id):
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            return jsonify(usuario), 200

    return jsonify({'erro': 'Usuario nao encontrado'}), 404

@users_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def atualizar_usuario(usuario_id):
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuario['nome'] = data.get('nome', usuario['nome'])
            usuario['email'] = data.get('email', usuario['email'])
            return jsonify(usuario), 200

    return jsonify({'erro': 'Usuario nao encontrado'}), 404


@users_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def deletar_usuario(usuario_id):

    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuario removido com sucesso'}), 200
            
    return jsonify({'erro': 'Usuario nao encontrado'}), 404        