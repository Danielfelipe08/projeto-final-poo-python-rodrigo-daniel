from bottle import get, post, request, redirect, template
from services.auth_service import ServicoAutenticacao
from data.gerenciador_dados import GerenciadorDados
from models.usuario_model import Admin, Leitor

# Instancia o banco
db_usuarios = GerenciadorDados("usuarios.json")

#ROTA AUXILIAR
@get('/setup')
def setup_inicial():
    """Cria usuários padrão se o JSON estiver vazio"""
    if not db_usuarios.ler_todos():
        admin = Admin(1, "Chefe", "admin@biblio.com", "admin123")
        leitor = Leitor(2, "Aluno", "aluno@biblio.com", "1234")
        db_usuarios.salvar_todos([admin.to_dict(), leitor.to_dict()])
        return "Dados iniciais criados! Login: admin@biblio.com / senha: admin123"
    return "Dados já existem."


@get('/login')
def login_form():
    return """
    <form action='/login' method='post'>
        Email: <input name='email' type='text' /><br>
        Senha: <input name='senha' type='password' /><br>
        <button type='submit'>Entrar</button>
    </form>
    """

@post('/login')
def login_processar():
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    
    usuario = ServicoAutenticacao.autenticar(email, senha)
    
    if usuario:
        ServicoAutenticacao.logar_usuario(usuario)
        return f"Bem-vindo, {usuario.nome}! <a href='/dashboard'>Ir para Dashboard</a>"
    else:
        return "Email ou senha inválidos. <a href='/login'>Tentar novamente</a>"

@get('/logout')
def logout():
    ServicoAutenticacao.deslogar()
    return redirect('/login')

@get('/dashboard')
@ServicoAutenticacao.admin_requerido
def dashboard():
    return "<h1>Painel Admin</h1> <p>Você tem permissão total.</p> <a href='/logout'>Sair</a>"