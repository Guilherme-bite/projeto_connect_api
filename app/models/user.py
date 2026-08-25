usuarios = [
    {
        "id": 1,
        "nome": "Guilherme",
        "email": "guilherme@example.com"
    }
]
proximo_id = 2

def criar_usuario(nome, email):
    global proximo_id

    novo_usuario = {
        "id": proximo_id,
        "nome": nome,
        "email": email
    }

    usuarios.append(novo_usuario)
    proximo_id += 1

    return novo_usuario