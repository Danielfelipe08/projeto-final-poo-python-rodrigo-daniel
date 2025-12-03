from bottle import Bottle, view, request, redirect
from services.livro_service import LivroService
from utils.auth_middleware import login_required

# Nome correto do router
livros_routes = Bottle()

# Instância do service
livro_service = LivroService()


# LISTAR LIVROS
@livros_routes.get("/livros")
@login_required
@view("livros/index")
def listar():
    livros = livro_service.listar()
    return dict(title="Livros", livros=livros)


# CRIAR LIVRO
@livros_routes.post("/livros")
@login_required
def criar():
    titulo = request.forms.get("titulo")
    autor = request.forms.get("autor")
    ano = request.forms.get("ano")

    livro_service.criar(titulo, autor, ano)

    return redirect("/livros")
