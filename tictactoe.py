from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        
        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))
            
            elif check_winner() is True:
                label.config(text=(players[0]+ " wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        
        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))
            
            elif check_winner() is True:
                label.config(text=(players[1]+ " wins"))
            
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

def check_winner():
    
    #Horizontal win conditions
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
        

    #Vertical win conditions
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True

    #Diagonal win conditions
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    
    #Tie conditions
    elif empty_spaces() is False:
        return "Tie"
    
    else:
        return False
    

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
reset_button.pack(side="bottom")

#Creating a frame for a window
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
