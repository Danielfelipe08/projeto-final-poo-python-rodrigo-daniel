from bottle import request, redirect

def login_required(fn):
    def wrapper(*args, **kwargs):
        session = request.environ.get("beaker.session")

        if not session or not session.get("user_id"):
            return redirect("/login")

        return fn(*args, **kwargs)
    return wrapper
