from models.user import UserModel, User

class UsuarioService:
    def __init__(self):
        self.model = UserModel()

    # LISTAR TODOS OS USUÁRIOS
    def listar(self):
        """Retorna lista completa de usuários"""
        return self.model.get_all()

    # CRIAR USUÁRIO
    def criar_usuario(self, name, email, birthdate):
        users = self.model.get_all()

        new_id = 1 if not users else max(u.id for u in users) + 1

        novo_usuario = User(
            id=new_id,
            nome=name,
            email=email,
            birthdate=birthdate
        )

        self.model.add_user(novo_usuario)
        return novo_usuario

    # AUTENTICAÇÃO
    def autenticar(self, email, birthdate):
        users = self.model.get_all()

        for user in users:
            if user.email == email and user.birthdate == birthdate:
                return user

        return None
