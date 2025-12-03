from bottle import static_file, request, template as render_template

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/static/<filename:path>', callback=self.serve_static)

    def get_session(self):
        return request.environ.get("beaker.session")

    def render(self, view_name, **context):
        session = self.get_session()

        context['session'] = session

        if "base" not in context:
            context["base"] = ""

        return render_template(view_name, **context)

    # STATIC FILE
    def serve_static(self, filename):
        return static_file(filename, root='./static')

    # REDIRECT
    def redirect(self, path, code=302):
        from bottle import response as bottle_response
        bottle_response.status = code
        bottle_response.set_header('Location', path)
        return bottle_response
