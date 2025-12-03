from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.auth_controller import auth_routes
from controllers.home_controller import home_routes
from .home_controller import home_routes
from controllers.livros_controller import livros_routes
from controllers.emprestimos_controller import emprestimos_routes


def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(auth_routes)
    app.merge(home_routes)
    app.mount("/", home_routes)
    app.merge(livros_routes)          
    app.merge(emprestimos_routes)    
