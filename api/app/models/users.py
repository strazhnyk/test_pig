from .shared import SqlAlchemyHelper, db


class User(db.Model, SqlAlchemyHelper):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    description = db.Column(db.String)
    employee = db.Column(db.Boolean)
