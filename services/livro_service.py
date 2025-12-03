import json
import os
from models.livro import Livro


class LivroService:
    def __init__(self):
        self.file_path = os.path.join("data", "livros.json")

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def listar(self):
        return [Livro.from_dict(l) for l in self._load()]

    def criar(self, titulo, autor, ano):
        livros = self._load()
        new_id = 1 if len(livros) == 0 else livros[-1]["id"] + 1

        livro = Livro(new_id, titulo, autor, ano)
        livros.append(livro.to_dict())
        self._save(livros)

        return livro
