import json
import os
from models.livro import Livro


class LivroService:
    def __init__(self):
        self.file_path = os.path.join("data", "livros.json")

        # Garante que o arquivo existe
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)


    # Carregar JSON

    def _load(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)

            # Caso o arquivo esteja vazio ou inválido
            if not isinstance(data, list):
                return []
            return data

        except json.JSONDecodeError:
            return []


    # Salvar JSON

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)


    # LISTAR LIVROS
    
    def listar(self):
        return [Livro.from_dict(l) for l in self._load()]


    # CRIAR LIVRO
   
    def criar(self, titulo, autor, ano):
        livros = self._load()

        # Gera ID seguro
        new_id = 1 if not livros else max(l["id"] for l in livros) + 1

        livro = Livro(new_id, titulo, autor, ano)

        livros.append(livro.to_dict())
        self._save(livros)

        return livro
