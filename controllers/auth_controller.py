from bottle import Bottle, get, post, view, request, redirect
from services.usuario_service import UsuarioService

auth_routes = Bottle()
usuario_service = UsuarioService()

def get_session():
    return request.environ.get("beaker.session")

def render_with_session(**kwargs):
    session = get_session()
    return dict(session=session, **kwargs)


# --- LOGIN PAGE ---
@auth_routes.get("/login")
@view("auth/login")
def login_page():
    return render_with_session(title="Login", error=None)


@auth_routes.post("/login")
def login_post():
    email = request.forms.get("email")
    birthdate = request.forms.get("birthdate")

    user = usuario_service.autenticar(email, birthdate)

    if user:
        session = get_session()

        if session is None:
            print("ERRO: Sessão está None! Middleware não carregou.")
            return "Erro interno: sessão não iniciada."

        session["user_id"] = user.id
        session.save()
        return redirect("/")

    return render_with_session(title="Login", error="Credenciais incorretas.")


# --- REGISTER PAGE ---
@auth_routes.get("/register")
@view("auth/register")
def register_page():
    return render_with_session(title="Cadastro", error=None)


@auth_routes.post("/register")
def register_post():
    name = request.forms.get("name")
    email = request.forms.get("email")
    birthdate = request.forms.get("birthdate")

    usuario_service.criar_usuario(name, email, birthdate)
    return redirect("/login")


# --- LOGOUT ---
@auth_routes.get("/logout")
def logout():
    session = get_session()
    if session:
        session.delete()
    return redirect("/login")
