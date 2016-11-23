from app import db

class Hist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20000))
    comment = db.Column(db.String(200))

    def __init__(self, number, comment):
        self.number = number
        self.comment = comment

    def __repr__(self):
        return '<Number %r>' %self.number + '<Comment %r>' %self.comment
