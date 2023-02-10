from config import db

class Cash(db.Model):
   id = db.Column(db.Integer, primary_key = True, nullable=False)
   cashTendered = db.Column(db.Float,nullable=False)
