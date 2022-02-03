from app import db

class Coffee(db.Model):
    __tablename__ = 'coffee'
    coffee_id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String, nullable=False, unique=True)
    type_coffee = db.Column(db.String, nullable=False)