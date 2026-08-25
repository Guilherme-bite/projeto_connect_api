from flask import Blueprint, jsonify, request
from app.models.user import usuarios, criar_usuario

users_bp = Blueprint('users', __name__)

@users_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@users_bp.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')

    novo_usuario = criar_usuario(nome, email)
    return jsonify(novo_usuario), 201