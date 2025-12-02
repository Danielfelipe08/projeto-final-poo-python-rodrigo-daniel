from bottle import Bottle, get, post, view, request, redirect
from services.usuario_service import UsuarioService

auth_routes = Bottle()
usuario_service = UsuarioService()


# --- LOGIN PAGE ---
@auth_routes.get("/login")
@view("auth/login")
def login_page():
    return dict(title="Login", error=None)


@auth_routes.post("/login")
@view("auth/login")
def login_post():
    email = request.forms.get("email")
    birthdate = request.forms.get("birthdate")   # <-- campo correto do modelo User

    user = usuario_service.autenticar(email, birthdate)

    if user:
        session = request.environ.get("beaker.session")
        session["user_id"] = user.id
        session.save()
        return redirect("/")
    else:
        return dict(
            title="Login",
            error="Credenciais incorretas."
        )


# --- REGISTER PAGE ---
@auth_routes.get("/register")
@view("auth/register")
def register_page():
    return dict(title="Cadastro", error=None)


@auth_routes.post("/register")
@view("auth/register")
def register_post():
    name = request.forms.get("name")              
    email = request.forms.get("email")
    birthdate = request.forms.get("birthdate")    

    usuario_service.criar_usuario(name, email, birthdate)

    return redirect("/login")


# --- LOGOUT ---
@auth_routes.get("/logout")
def logout():
    session = request.environ.get("beaker.session")
    session.delete()
    return redirect("/login")
