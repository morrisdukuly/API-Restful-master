from config import db


class Check(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    name = db.Column(db.String(120),nullable=False)
    bankID = db.Column(db.String(120),nullable=False)