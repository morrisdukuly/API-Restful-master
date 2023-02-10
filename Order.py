from config import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    createDate = db.Column(db.Date,nullable=False)
