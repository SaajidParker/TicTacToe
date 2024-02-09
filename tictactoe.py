from tkinter import *
import random

def next_turn(row, column):
    pass

def check_winner():
    pass

def empty_spaces():
    pass

def new_game():
    pass

#Creating a window
window = Tk()

#Window title
window.title("Tic-Tac-Toe")

#Creating Players
players = ["X", "O"]
#Selecting starter player
player = random.choice(players)

#Buttons for the grid initializing them
buttons = []
for _ in range(3):
    row = []
    for _ in range(3):
        row.append(None)
    buttons.append(row)

#Label for player turn
label = Label(text= player + "'s Turn", font=('consolas', 40))
label.pack(side="top")

#Creating reset button
reset_button = Button(text="Restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

#Creating a frame for a window
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
