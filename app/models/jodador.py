from app import db

class Jogador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    jogador_clube = db.Column(db.String(100),nullable=False)
    jogador_nacao = db.Column(db.String(100), nullable=False)
    foto = db.Column(db.String(200))