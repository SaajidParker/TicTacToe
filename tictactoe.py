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

#Label for player turn
label = Label(text= player + "'s Turn", font =('consolas',40))
label.pack(side="top")

#Creating reset button
reset_button = Button(text="Restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

window.mainloop()