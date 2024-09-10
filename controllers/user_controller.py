# controllers/user_controller.py
from models.user import db, User

def get_all_users():
    """Retorna todos os usuários"""
    return User.query.all()

def get_user_by_id(user_id):
    """Obtém um usuário pelo ID"""
    return User.query.get_or_404(user_id)

def create_user(data):
    """Cria um novo usuário"""
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, data):
    """Atualiza um usuário existente pelo ID"""
    user = get_user_by_id(user_id)
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return user

def delete_user(user_id):
    """Deleta um usuário pelo ID"""
    user = get_user_by_id(user_id)
    db.session.delete(user)
    db.session.commit()

def get_user_by_name(name):
    """Busca usuários pelo nome usando filtro LIKE"""
    users = User.query.filter(User.name.ilike(f'%{name}%')).all()
    if not users:
        raise ValueError("Usuário não encontrado")
    return users
