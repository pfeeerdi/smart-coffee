from flask import Flask
from app.config import Config, BackupConfig
from flask_cors import CORS
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy

#from app.create_db import create_db
db = SQLAlchemy()
mqtt = Mqtt()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mqtt.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        from app.model import Coffee
        db.create_all()
        print("DB connected")
        from app.service.coffee_service import update_coffee_hist
        update_coffee_hist()

    from app.controller import blueprint as api
    app.register_blueprint(api, url_prefix="")

    CORS(app, support_credentials=False)
    return app