from flask import Flask
from flask_migrate import Migrate
from .database import db
import os

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = "oz_kwak_coding"

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dbfile = os.path.join(basedir, "db.sqlite")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main as main_blp, admin as admin_blp

    app.register_blueprint(main_blp)
    app.register_blueprint(admin_blp)

    return app
