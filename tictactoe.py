from tkinter import *
import random

def next_turn():
    pass

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

#Creatiug a window
window = Tk()

#Window title
window.title("Tic-Tac-Toe")

#Creating Players
players = ["X","O"]
#Selecting starter player
player = random.choice(players)

#Buttons for the grid
button = [[0,0,0],
          [0,0,0],
          [0,0,0]]

window.mainloop()