from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.auth_controller import auth_routes
from controllers.home_controller import home_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(auth_routes)
    app.merge(home_routes)
