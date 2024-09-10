# app.py
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from models.user import db
from views.user_view import ns as user_namespace

app = Flask(__name__)
CORS(app)
app.config.from_object('config.Config')

# Inicializa o banco de dados
db.init_app(app)

# Inicializa a API e adiciona o namespace
api = Api(app, doc='/docs', title='User API', description='API para gerenciar usuários')
api.add_namespace(user_namespace, path='/users')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
