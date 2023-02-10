from config import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    deliveryAddress = db.Column(db.String(120),nullable=False)
    Contact = db.Column(db.String(120),nullable=False)
    active = db.Column(db.Boolean(120),nullable=False)