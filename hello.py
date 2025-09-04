# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def home():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<nome>')
def user(nome):
    return render_template('user.html', nome=nome)

@app.route('/rotainexistente')
def erro():
    return render_template('404.html')
