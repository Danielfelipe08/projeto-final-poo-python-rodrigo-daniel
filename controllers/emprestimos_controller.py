from bottle import Bottle, view, request, redirect
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.usuario_service import UsuarioService
from utils.auth_middleware import login_required

emprestimos_routes = Bottle()   

emprestimo_service = EmprestimoService()
livro_service = LivroService()
usuario_service = UsuarioService()

@emprestimos_routes.get("/emprestimos")
@login_required
@view("emprestimos/index")
def listar():
    emprestimos = emprestimo_service.listar()
    livros = {l.id: l.titulo for l in livro_service.listar()}
    usuarios = {u.id: u.name for u in usuario_service.listar()}

    return dict(
        title="Empréstimos",
        emprestimos=emprestimos,
        livros=livros,
        usuarios=usuarios
    )

@emprestimos_routes.post("/emprestimos")
@login_required
def criar():
    usuario_id = int(request.forms.get("usuario_id"))
    livro_id = int(request.forms.get("livro_id"))
    data = request.forms.get("data")

    emprestimo_service.criar(usuario_id, livro_id, data)

    return redirect("/emprestimos")
