from flask import Flask
from flask_bootstrap import Bootstrap
from config import configOptions

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #create app configuraions
    app.config.from_object(configOptions[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configRequest
    configRequest(app)


    return app