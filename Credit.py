from config import db

class Credit(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    number = db.Column(db.Float,nullable=False)
    type = db.Column(db.String(120),nullable=False)
    expireDate = db.Column(db.Date(),nullable=False)
