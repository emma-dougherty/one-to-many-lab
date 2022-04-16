from models.player import *
from models.choice import *

def result(player1, player2):

    if player2.choice == "Rock" and player1.choice == "Scissors":
        player2.winner = "Winner"
    if player2.choice == "Scissors" and player1.choice == "Paper":
        player2.winner = "Winner"
    if player2.choice == "Paper" and player1== "Rock":
        player2.winner = "Winner"

    if player1.choice == "Rock" and player2.choice == "Scissors":
        player1.winner = "Winner"
    if player1.choice == "Scissors" and player2.choice == "Paper":
        player1.winner = "Winner"
    if player1.choice == "Paper" and player2== "Rock":
        player1.winner = "Winner"

    
    if player1.choice == player2.choice:
        player1.winner = "Tie"
        player2.winner = "Tie"


