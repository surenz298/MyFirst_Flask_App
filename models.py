from app import db

class Hist(db.Model):
    number = db.Column(db.String(20000), primary_key=True)
    comment = db.Column(db.String(2000), primary_key=True)

    def __init__(self, number, comment):
        self.number = number
        self.comment = comment

    def __repr__(self):
        return '<Number %r>' %self.number + '<Comment %r>' %self.comment
