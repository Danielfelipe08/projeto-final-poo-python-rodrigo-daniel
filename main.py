from beaker.middleware import SessionMiddleware
from bottle import run
from app import create_app

session_opts = {
    "session.type": "memory",
    "session.cookie_expires": 3600,
    "session.auto": True
}

if __name__ == "__main__":
    app = create_app()
    app.setup_routes()

    wsgi_app = SessionMiddleware(app.bottle, session_opts)

    run(
        app=wsgi_app,
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        reloader=app.config.RELOADER
    )
