from tkinter import *
import tkinter.messagebox
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player
        if player == "X":
            buttons[row][column].config(bg="lightblue")  # Change background color to light blue for X
        elif player == "O":
            buttons[row][column].config(bg="lightcoral")  # Change background color to light red for O
        
        winner = check_winner()  # Store the result of check_winner() in a variable

        if winner:
            label.config(text=f"{player} wins")
            tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is {player}")
        elif winner == "Tie":
            label.config(text="Match is Draw!")  # Update label text for tie
            tkinter.messagebox.showinfo("Tic Tac Toe", "Match is Draw.")
        else:
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player}'s turn")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_winner([buttons[row][0], buttons[row][1], buttons[row][2]])
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            highlight_winner([buttons[0][column], buttons[1][column], buttons[2][column]])
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([buttons[0][0], buttons[1][1], buttons[2][2]])
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([buttons[0][2], buttons[1][1], buttons[2][0]])
        return True
    elif not empty_spaces():
        return "Tie"  # Returning "Tie" here if there's no winner
    return False


def highlight_winner(cells):
    for cell in cells:
        cell.config(bg="lightgreen")

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player}'s turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="SystemButtonFace")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)

label = Label(text=f"{player}'s Turn", font=('Helvetica', 20))  # Change the font to Helvetica
label.pack(side="top")

reset_button = Button(text="Restart", font=('Arial', 12), command=new_game)
reset_button.pack(side="bottom", pady=10)

frame = Frame(window, bg="beige")  # Set the background color of the frame
frame.pack(padx=20, pady=20)  # Add padding around the frame

buttons = []
for row in range(3):
    button_row = []
    for column in range(3):
        button = Button(frame, text="", font=('Arial', 20), width=5, height=2,
                        command=lambda row=row, column=column: next_turn(row, column),bg="white")
        button.grid(row=row, column=column, padx=5, pady=5)  # Add padding around each button
        button_row.append(button)
    buttons.append(button_row)

window.mainloop()
