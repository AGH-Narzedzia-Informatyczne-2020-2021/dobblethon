#                            #
#   Dobblethon Core v0.1.0   #
#                            #
##############################
#
#   Large scale check for whether the card algorithms are correct is needed, should be good tho
#
#   !!!!! MOVE OVERLAPING ELEMENTS TO THE BEGINING OF THE CARD LIST !!!!!
#       Mind that each card's images data is stored in the following format:
#       [0]-[PLAYER_COUNT-1]       - overlaping items, in specific order (player1, player2, ... playern, table)
#       [PLAYER_COUNT]-[CARD_SIZE] - unique items
#       After new card is generated during the game, the current cards need to hold to this format
#       TODO: When working on the in-game functions, remember to make one shuffling the elements in a way the format is kept
#       NOTE: Function generating new table card generates the table overlaping items, so it interprets [PLAYER_COUNT-1] element as unique one   
#
#   range(a,b+1)   ->   <a, b>
#   randint(a,b)   ->   <a, b>
#

import random

# Constants
BANK_SIZE = 55                          # Defines amount of all available pictures 
CARD_SIZE = 10                          # Defines amount of pictures on a single card

# User input variables (TODO change to user input)
PLAYER_COUNT = 4                        # Defines amount of players in game

# Variables
BoardCards = [[],[],[],[],[]]          # Holds current cards' info [table], [player1], [player2], [player3], [player4]

# Functions

# Core
#   Generate initial users' cards
BoardCards[0] = list(range(1,BANK_SIZE+1))
random.shuffle(BoardCards[0])
for i in range (1, PLAYER_COUNT+1):    
    BoardCards[i] = BoardCards[i][0:i-1] + BoardCards[0][:CARD_SIZE-i+1]
    for j in range (i+1, PLAYER_COUNT+1):    
        BoardCards[j].append(BoardCards[i][j-2])
    BoardCards[0] = BoardCards[0][CARD_SIZE-i+1:]

#   Generate initial table card
#   To be defined as a function
BoardCards[0] = list(range(CARD_SIZE))
for i in range(CARD_SIZE):
    BoardCards[0][i] = 0
for i in range(0, PLAYER_COUNT):
    BoardCards[0][i] = BoardCards[i+1][CARD_SIZE-1]
    BoardCards[i+1][CARD_SIZE-1], BoardCards[i+1][PLAYER_COUNT-1] = BoardCards[i+1][PLAYER_COUNT-1], BoardCards[i+1][CARD_SIZE-1]
i += 1
while i < CARD_SIZE:
    BoardCards[0][i] = random.randint(1, BANK_SIZE)
    for j in range(CARD_SIZE*PLAYER_COUNT+1):
        if BoardCards[0][i] == BoardCards[(j//10)][j%10] and j != i:
            i -= 1
            ### DEBUG
            #print("found the same item at", (j//10)+1, j%10)
            break
    i += 1





for i in range(PLAYER_COUNT+1):
    #BoardCards[i].sort() ### DEBUG
    print(BoardCards[i])


