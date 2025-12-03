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
    # 1. FIX: Pegar a sessão do Beaker para evitar erro no layout
    session = request.environ.get('beaker.session')

    emprestimos = emprestimo_service.listar()
    livros = {l.id: l.titulo for l in livro_service.listar()}
    
    # 2. FIX: Mudado de u.name para u.nome (pois o modelo está em português)
    usuarios = {u.id: u.nome for u in usuario_service.listar()}

    return dict(
        title="Empréstimos",
        emprestimos=emprestimos,
        livros=livros,
        usuarios=usuarios,
        session=session # 3. FIX: Passar a sessão para o template
    )

@emprestimos_routes.post("/emprestimos")
@login_required
def criar():
    # Tenta converter para int, mas protege caso venha vazio (opcional, mas recomendado)
    try:
        usuario_id = int(request.forms.get("usuario_id"))
        livro_id = int(request.forms.get("livro_id"))
    except (ValueError, TypeError):
        return redirect("/emprestimos") # Ou retornar erro

    data = request.forms.get("data")

    emprestimo_service.criar(usuario_id, livro_id, data)

    return redirect("/emprestimos")