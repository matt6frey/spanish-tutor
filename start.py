from game_utils.functions import *
from game_utils.player.Player import Player
from game_utils.Game import Game

if __name__ == "__main__":
    # start game
    player_name = ''
    while player_name == '' or player_name == None:
        player_name = input("What's your name?\n")
        if player_name == '' or player_name == None:
            print("Please try again...\n")
    num_of_questions = ''
    while not num_of_questions.isdigit():
        num_of_questions = input("How many questions do you want to practice today?\n")
        if num_of_questions == '' or num_of_questions == None or not num_of_questions.isdigit():
            print("Please try again...\n")
    player = Player(player_name)
    game = Game(number_of_questions=int(num_of_questions), player=player)
    game.play()
    print("Thanks for playing!\n")
