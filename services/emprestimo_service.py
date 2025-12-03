import json
import os
from models.emprestimo import Emprestimo

class EmprestimoService:
    def __init__(self):
        self.file_path = os.path.join("data", "emprestimos.json")

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
        return [Emprestimo.from_dict(e) for e in self._load()]

    def criar(self, usuario_id, livro_id, data):
        emprestimos = self._load()
        new_id = 1 if len(emprestimos) == 0 else emprestimos[-1]["id"] + 1

        emp = Emprestimo(new_id, usuario_id, livro_id, data)
        emprestimos.append(emp.to_dict())
        self._save(emprestimos)

        return emp
