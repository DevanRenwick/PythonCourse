# Here are the requirements:
#
# 2 players should be able to play the game (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
# Feel free to use Google to help you figure anything out (but don't just Google "Tic Tac Toe in Python" otherwise you won't learn anything!)
# Keep in mind that this project can take anywhere between several hours to several days.
#
# There are 4 Jupyter Notebooks related to this assignment:
#
# This Assignment Notebook
# A "Walkthrough Steps Workbook" Notebook
# A "Complete Walkthrough Solution" Notebook
# An "Advanced Solution" Notebook

def display(row1, row2, row3):
    # Displays the board for players.
    print(row1)
    print(row2)
    print(row3)

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

print("This is my tic tac toe game")
display(row1, row2, row3)