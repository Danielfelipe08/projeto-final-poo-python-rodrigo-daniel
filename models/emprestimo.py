class Emprestimo:
    def __init__(self, id, usuario_id, livro_id, data):
        self.id = id
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data = data  # string "2025-02-02"

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "livro_id": self.livro_id,
            "data": self.data
        }

    @staticmethod
    def from_dict(data):
        return Emprestimo(
            id=data["id"],
            usuario_id=data["usuario_id"],
            livro_id=data["livro_id"],
            data=data["data"]
        )
