from config import db

  

class WireTransfer(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    bankID = db.Column(db.String(120),nullable=False)
    bankName = db.Column(db.String(120),nullable=False)

