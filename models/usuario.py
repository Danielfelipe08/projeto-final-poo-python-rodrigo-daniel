class Usuario:
    def __init__(self, id, nome, email, senha, papel="comum"):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.papel = papel  # 'comum' ou 'admin'

    def eh_admin(self):
        """Verifica se o utilizador é administrador."""
        return self.papel == "admin"

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "papel": self.papel,
        }


class UsuarioComum(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha, papel="comum")

    def permissao(self):
        return "Acesso básico ao sistema"


class UsuarioAdmin(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha, papel="admin")

    def permissao(self):
        return "Acesso total ao sistema (admin)"
