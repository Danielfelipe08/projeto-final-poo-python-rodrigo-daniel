from bottle import Bottle, view
from utils.auth_middleware import login_required
from controllers.auth_controller import get_session

home_routes = Bottle()

@home_routes.get("/")
@login_required
@view("home/index")
def home():
    session = get_session()  

    return dict(
        title="Início",
        session=session   
    )
