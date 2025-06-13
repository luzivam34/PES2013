from app import db

class Jogadorpes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    posicao = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    clube = db.Column(db.String(100), nullable=False)
    nation = db.Column(db.String(100), nullable=False)
