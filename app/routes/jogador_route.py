from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models.jogadore_models import Jogadorpes
from app.models.jodador import Jogador

jogador_bp = Blueprint('jogador', __name__)

@jogador_bp.route('/')
@jogador_bp.route('/jogador')
def listar_jogador():
    jogador = Jogadorpes.query.order_by(Jogadorpes.nome).all()
    #jogador1 = Jogador.query.order_by(Jogador.nome).all()
    return render_template('jogador/jogador.html', jogador=jogador)

@jogador_bp.route('/jogador/cadastro', methods=['POST','GET'])
def cadastro_de_Jogadores():
    if request.method == 'POST':
        nome = request.form['nome']
        posicao = request.form['posicao']
        idade = request.form['idade']
        clube = request.form['clube']
        nation = request.form['nation']

        jogador = Jogadorpes(nome=nome, posicao=posicao, idade=idade, clube=clube, nation= nation)
        db.session.add(jogador)
        db.session.commit()
        return redirect( url_for('jogador.listar_jogador'))
    return render_template('jogador/cadastro_de_jogadores.html')