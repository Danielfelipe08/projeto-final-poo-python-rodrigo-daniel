class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano
        }

    @staticmethod
    def from_dict(data):
        return Livro(
            id=data["id"],
            titulo=data["titulo"],
            autor=data["autor"],
            ano=data["ano"]
        )
