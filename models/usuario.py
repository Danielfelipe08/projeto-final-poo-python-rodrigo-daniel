class Usuario:
    def __init__(self, nome_usuario, senha, papel='comum'):
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.papel = papel  # 'comum' ou 'admin'

    def eh_admin(self):
        """Verifica se o utilizador é administrador."""
        return self.papel == 'admin'