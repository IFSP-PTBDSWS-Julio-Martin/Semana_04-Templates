# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def home():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):
    return render_template(
        'user.html',
        nome=nome,
        prontuario=prontuario,
        instituicao=instituicao
    )

@app.route('/contexto/<nome>')
def contexto(nome):
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.host
    return render_template(
        'contexto.html',
        nome=nome,
        user_agent=user_agent,
        ip=ip,
        host=host
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
