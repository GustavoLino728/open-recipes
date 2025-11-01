# backend/app/__init__.py
from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.routes.receitas import receitas_bp

def create_app():
    """Factory para criar a aplicação Flask"""
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app, 
         resources={r"/api/*": {"origins": "*"}},
         supports_credentials=False,
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    )
    
    app.register_blueprint(receitas_bp)
    
    @app.route('/')
    def index():
        return {
            'message': 'API Backend - Receitas App',
            'status': 'running'
        }
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    return app