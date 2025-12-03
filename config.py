import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Configurações do servidor
    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    # Paths
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    # Outras configurações
    SECRET_KEY = 'sua-chave-secreta-aqui'

    # 🚀 CONFIGURAÇÃO DE SESSÃO — ESSENCIAL PARA LOGIN FUNCIONAR
    SESSION_OPTS = {
        'session.type': 'file',
        'session.cookie_expires': 3600,
        'session.data_dir': os.path.join(BASE_DIR, 'data', 'sessions'),
        'session.auto': True
    }
