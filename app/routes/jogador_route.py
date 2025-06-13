from flask import Blueprint, render_template
from app.models.jogadore_models import Jogadorpes

jogador_bp = Blueprint('jogador', __name__)

@jogador_bp.route('/')
@jogador_bp.route('/jogador')
def listar_jogador():
    jogador = Jogadorpes.query.order_by(Jogadorpes.nome).all()
    return render_template('jogador.html', jogador=jogador)