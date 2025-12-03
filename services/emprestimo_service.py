import json
import os
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self):
        self.file_path = os.path.join("data", "emprestimos.json")

        # Garante que o arquivo existe
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

 
    # Carregar JSON
   
    def _load(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                return []
            return data
        except json.JSONDecodeError:
            return []

   
    # Salvar JSON
   
    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    # Listar empréstimos
 
    def listar(self):
        return [Emprestimo.from_dict(e) for e in self._load()]

 
    # Criar novo empréstimo
 
    def criar(self, usuario_id, livro_id, data):
        emprestimos = self._load()

        # ID seguro e imune à bagunça
        new_id = 1 if not emprestimos else max(e["id"] for e in emprestimos) + 1

        emp = Emprestimo(new_id, usuario_id, livro_id, data)
        emprestimos.append(emp.to_dict())
        self._save(emprestimos)

        return emp
