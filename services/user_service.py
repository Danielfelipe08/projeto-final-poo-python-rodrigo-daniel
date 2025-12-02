from bottle import request
from models.user import UserModel, User

class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def get_all(self):
        return self.user_model.get_all()

    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1

        nome = request.forms.get('nome')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        papel = request.forms.get('papel', 'commum')  

        # Criando novo usuário
        user = User(
            id=new_id,
            nome=nome,
            email=email,
            birthdate=birthdate,
            papel=papel
        )

        self.user_model.add_user(user)

    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)

    def edit_user(self, user):
        # Novos valores vindos do formulário
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        papel = request.forms.get('papel', user.papel)

        # Atualizando os atributos corretamente
        user.nome = nome
        user.email = email
        user.birthdate = birthdate
        user.papel = papel

        self.user_model.update_user(user)

    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
