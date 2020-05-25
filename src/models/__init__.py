from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

bcrypt = Bcrypt()

from .task_model import TaskModel, TaskSchema
from .user_model import UserModel, UserSchema