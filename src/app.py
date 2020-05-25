from flask import Flask

from .config import app_config
from .models import db, bcrypt
from .views.user_view import user_api as user_blueprint
from .views.task_view import  task_api as task_blueprint

def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(task_blueprint, url_prefix='/api/v1/tasks')

    return app