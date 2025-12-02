from abc import ABC, abstractmethod

#ABSTRAÇÃO: classe modelo que não pode ser instanciada diretamente
class Usuario(ABC):
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        #ENCAPSULAMENTO: A senha é protegida (privada)
        self.__senha = senha 

    def verificar_senha(self, senha_texto):
        """Método seguro para checar senha sem expor o atributo privado"""
        return self.__senha == senha_texto

    # POLIMORFISMO (Abstrato): Cada filho DEVE implementar este método do seu jeito
    @abstractmethod
    def tem_permissao_admin(self):
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.__senha,
            "tipo": self.__class__.__name__ # Salva se é 'Admin' ou 'Leitor'
        }

# 4. HERANÇA: Admin herda de Usuario
class Admin(Usuario):
    def tem_permissao_admin(self):
        return True  # Polimorfismo: Admin retorna Verdadeiro

# 4. HERANÇA: Leitor herda de Usuario
class Leitor(Usuario):
    def tem_permissao_admin(self):
        return False # Polimorfismo: Leitor retorna Falso