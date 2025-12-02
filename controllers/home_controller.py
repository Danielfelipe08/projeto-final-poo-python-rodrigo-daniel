from bottle import Bottle, view
from utils.auth_middleware import login_required

home_routes = Bottle()

@home_routes.get("/")
@login_required
@view("home/index")
def home():
    return dict(title="Home")
