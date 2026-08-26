# projeto_connect_api
API REST em Flask para CRUD de usuários — projeto de estudo com foco em boas práticas de arquitetura back-end.

# API Connect

API REST para gerenciamento de usuários, desenvolvida em Python com o microframework Flask. O projeto representa o back-end de um MVP (Produto Mínimo Viável) para uma startup de tecnologia, fornecendo operações de cadastro, listagem, busca, atualização e remoção de usuários (CRUD completo) seguindo os padrões da arquitetura REST.

## Objetivo

Fornecer uma base sólida e organizada de API REST, capaz de atender requisições HTTP de um front-end, com persistência provisória de dados em memória, validação de entrada, padronização de respostas em JSON e uso correto dos códigos de status HTTP.

## Tecnologias utilizadas

- **Python 3.14**
- **Flask** — microframework web, responsável pelo roteamento e tratamento das requisições HTTP
- **Flask-CORS** — habilita o consumo da API por aplicações front-end hospedadas em outros domínios/portas
- **python-dotenv** — gerenciamento de variáveis de ambiente

## Estrutura do projeto

connect_api_guilherme_santos/
├── app/
│   ├── __init__.py       # Application factory (create_app) e registro de rotas
│   ├── models/
│   │   └── user.py       # Estrutura de dados em memória e lógica de criação de usuários
│   └── routes/
│       └── users.py      # Rotas HTTP (GET, POST, PUT, DELETE) de usuários
├── run.py                # Ponto de entrada da aplicação
├── requirements.txt      # Dependências do projeto
└── .gitignore

## Como executar o projeto localmente

1. Clone o repositório:
```bash
git clone https://github.com/Guilherme-bite/projeto_connect_api_guilherme_santos.git
cd projeto_connect_api_guilherme_santos.git
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute o servidor:
```bash
python run.py
```

5. A API estará disponível em `http://127.0.0.1:5000`

## Endpoints

| Método | Rota | Descrição | Status de sucesso |
|--------|------|-----------|-------------------|
| GET | `/usuarios` | Lista todos os usuários cadastrados | 200 |
| POST | `/usuarios` | Cadastra um novo usuário | 201 |
| GET | `/usuarios/<id>` | Busca um usuário específico pelo ID | 200 (ou 404 se não encontrado) |
| PUT | `/usuarios/<id>` | Atualiza os dados de um usuário existente | 200 (ou 404 se não encontrado) |
| DELETE | `/usuarios/<id>` | Remove um usuário existente | 200 (ou 404 se não encontrado) |

### Exemplos de uso

**Listar usuários**
```http
GET /usuarios
```
Resposta (200):
```json
[
  { "id": 1, "nome": "Guilherme", "email": "guilherme@example.com" }
]
```

**Cadastrar usuário**
```http
POST /usuarios
Content-Type: application/json

{
  "nome": "Maria",
  "email": "maria@email.com"
}
```
Resposta (201):
```json
{
  "data": {
    "id": 2,
    "nome": "Maria",
    "email": "maria@email.com"
  }
}
```

Resposta de erro caso `nome` ou `email` não sejam enviados (400):
```json
{
  "erro": "Nome e email sao obrigatorios"
}
```

**Buscar usuário por ID**
```http
GET /usuarios/1
```
Resposta (200):
```json
{ "id": 1, "nome": "Guilherme", "email": "guilherme@example.com" }
```

Resposta caso o ID não exista (404):
```json
{ "erro": "Usuario nao encontrado" }
```

**Atualizar usuário**
```http
PUT /usuarios/1
Content-Type: application/json

{
  "nome": "Guilherme Santos"
}
```
Resposta (200):
```json
{ "id": 1, "nome": "Guilherme Santos", "email": "guilherme@example.com" }
```

**Remover usuário**
```http
DELETE /usuarios/1
```
Resposta (200):
```json
{ "mensagem": "Usuario removido com sucesso" }
```

## Autor

Guilherme Santos