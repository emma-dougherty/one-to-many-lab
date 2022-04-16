from flask import render_template, request, redirect
from app import app
from models.game import *
from models.player import *
from models.choice import *
from models.game import *

@app.route('/')
def index():
    return render_template('index.html', title ='Home')

@app.route('/choice')
def choice():
    clear_players()
    return render_template('choice.html', title ='Player1', players=players)

@app.route('/choice', methods = ['POST'])
def add_choice():
    print(request.form)
    name = request.form['name']
    choice=request.form['choice']
    player = Player(name,choice,"")
    add_player_choice(player)
    print([players])
    return redirect('/choice_2')

@app.route('/choice_2')
def choice_2():
    return render_template('choice_2.html', title ='Player2', players=players)

@app.route('/choice_2', methods = ['POST'])
def add_choice_2():
    print(request.form)
    name = request.form['name']
    choice=request.form['choice']
    player = Player(name,choice,"")
    add_player_choice(player)
    print([players])
    return redirect('/result')

@app.route('/result')
def get_result():
    player1 = players[0]
    player2 = players[1]
    result(player1,player2)
    return render_template('result.html', title = "Result", players=players)

# @app.route('/result/clear')
# def clear_players():
#     return redirect('/choice', title = "Result", players=players)

