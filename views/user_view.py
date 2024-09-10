# views/user_view.py
from flask import request
from flask_restx import Namespace, Resource, fields
from controllers.user_controller import (
    get_all_users, get_user_by_id, create_user, update_user, delete_user, get_user_by_name
)

ns = Namespace('users', description='Operações de usuários')

user_model = ns.model('User', {
    'id': fields.Integer(readonly=True, description='Identificador único'),
    'name': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário')
})

@ns.route('/')
class UserList(Resource):
    @ns.doc('list_users')
    @ns.marshal_list_with(user_model)
    def get(self):
        """Lista todos os usuários"""
        return get_all_users()

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """Cria um novo usuário"""
        return create_user(request.json), 201

@ns.route('/<int:id>')
@ns.response(404, 'Usuário não encontrado')
@ns.param('id', 'Identificador do usuário')
class UserResource(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, id):
        """Obtém um usuário pelo ID"""
        return get_user_by_id(id)

    @ns.doc('delete_user')
    @ns.response(204, 'Usuário deletado')
    def delete(self, id):
        """Deleta um usuário pelo ID"""
        delete_user(id)
        return '', 204

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, id):
        """Atualiza um usuário pelo ID"""
        return update_user(id, request.json)

@ns.route('/search')
@ns.param('name', 'Nome do usuário')
class UserSearch(Resource):
    @ns.doc('search_user')
    @ns.marshal_with(user_model)
    def get(self):
        """Busca um usuário pelo nome"""
        name = request.args.get('name')
        return get_user_by_name(name)
