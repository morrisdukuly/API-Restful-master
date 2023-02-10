from config import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    amount = db.Column(db.Float,nullable=False)
    payment_mode = db.Column(db.String(120),nullable=False)
