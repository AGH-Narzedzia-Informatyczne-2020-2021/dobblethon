#                            #
#   Dobblethon Core v0.1.1   #
#                            #
##############################  
#
#   range(a,b)     ->   <a, b-1>
#   randint(a,b)   ->   <a, b>
#
#   Constants can't be freely edited, specific relations between the values need to be held in order for the game to run properly
#   TODO Write down relations; we need these rules if we enable customizing a game
#   TODO Add code to send back cards,
#

# Libraries
import random

# Constants
BANK_SIZE = 55                          # Amount of all available pictures 
CARD_SIZE = 10                          # Amount of pictures on a single card
TOTAL_SCORE = 50                        # Amount of points (cards) available to collect (obsolete if GAMEMODE == 2)
MAX_SCORE = 3                           # Amount of points (collected cards) required for a single player to win (obsolete if GAMEMODE == 1)
SCORE_LIMITS = [TOTAL_SCORE, MAX_SCORE]
ITEM_NAMES = [                          # Holds item names; NOTE not yet defined, for now it's managed by code in #Core

]

# User input variables (TODO change to user input)
PLAYER_COUNT = 4                        # Defines amount of players in game
GAMEMODE = 2                            # Defines game mode; 1 - top player after TOTAL_SCORE is reached wins, 2 - first to score MAX_SCORE wins

# Variables
BoardCards = [[],[],[],[],[]]           # Holds current cards' info; [table], [player1], [player2], [player3], [player4]     TODO - length needs to be defined by PLAYER_COUNT
PlayerScore = [0, 0, 0, 0, 0, 0]        # Holds top player's number and players' score; [total-score], [top-player-score], [player1-score]...    TODO - same thing ^
ClientInput = []                        # Collects input from clients; Input format: 'Ab': A - player code, b - word

# Functions
def PrintCards(n):
    #   Print out cards on console
    #       n=0 - keep items order
    #       n=1 - sort items
    #       n=2 - shuffle items
    for i in range(PLAYER_COUNT+1):
        if n==0:
            out = BoardCards[i]
        if n==1:
            out = BoardCards[i]
            out.sort()
        if n==2:
            out = BoardCards[i]
            random.shuffle(out)
        print(out)

def FindOverlappingItems():
    # Very inefficient, it just works
    j = (PLAYER_COUNT+1)*CARD_SIZE
    for i in range(j**2):
        if BoardCards[(i//j)//CARD_SIZE][(i//j)%CARD_SIZE] == BoardCards[(i%j)//CARD_SIZE][(i%j)%CARD_SIZE] and i//j != i%j:
            #these overlap, add needed instruction here
            print()

def GenTableCard():
    BoardCards[0] = list(range(CARD_SIZE))
    for i in range(CARD_SIZE):
        BoardCards[0][i] = 0
    for i in range(0, PLAYER_COUNT):
        BoardCards[0][i] = BoardCards[i+1][CARD_SIZE-1]
        BoardCards[i+1][CARD_SIZE-1], BoardCards[i+1][PLAYER_COUNT-1] = BoardCards[i+1][PLAYER_COUNT-1], BoardCards[i+1][CARD_SIZE-1]
        j = random.randint(PLAYER_COUNT, CARD_SIZE-1)
        BoardCards[i+1][CARD_SIZE-1], BoardCards[i+1][j] = BoardCards[i+1][j], BoardCards[i+1][CARD_SIZE-1]
    i += 1
    while i < CARD_SIZE:
        BoardCards[0][i] = random.randint(1, BANK_SIZE)
        for j in range(CARD_SIZE*(PLAYER_COUNT+1)):
            if BoardCards[0][i] == BoardCards[(j//CARD_SIZE)][j%CARD_SIZE] and j != i:
                ### DEBUG
                #print("found the same item at", (j//CARD_SIZE), j%CARD_SIZE)
                #print(BoardCards[0])
                #print(BoardCards[j//CARD_SIZE])
                i -= 1
                break
        i += 1


# Core
#   Set up user input variables
#   TODO do this
print("GAMEMODE =", GAMEMODE)
print("PLAYER_COUNT = ", PLAYER_COUNT)
print()

#   Generate initial users' cards
BoardCards[0] = list(range(1,BANK_SIZE+1))
random.shuffle(BoardCards[0])
for i in range (1, PLAYER_COUNT+1):    
    BoardCards[i] = BoardCards[i][0:i-1] + BoardCards[0][:CARD_SIZE-i+1]
    for j in range (i+1, PLAYER_COUNT+1):    
        BoardCards[j].append(BoardCards[i][j-2])
    BoardCards[0] = BoardCards[0][CARD_SIZE-i+1:]

#   Generate initial table card
GenTableCard()

#   Get item names 
#   NOTE Item names are to be predefined, this code is obsolete after it's done
ITEM_NAMES = list(range(100))
for i in range(100):
    ITEM_NAMES[i] = str(i)

#   Run match
#   With makeshift console interface 
#   NOTE GUI is to be handled by client scripts, this is the server script
while PlayerScore[GAMEMODE-1] < SCORE_LIMITS[GAMEMODE-1]:
    PrintCards(0)
    ### DEBUG Print table paired items
    #print(BoardCards[0][:4])
    while len(ClientInput) == 0:
        #input() is makeshift, append ClientInput with Socket lib instead
        #TODO import with Socket
        ClientInput.append(input())
    if ClientInput[0][1:] == ITEM_NAMES[BoardCards[int(ClientInput[0][0])][PLAYER_COUNT-1]]:
        PlayerScore[0] += 1                             #total score used for GAMEMODE = 1
        PlayerScore[int(ClientInput[0][0])+1] += 1      #player score used for GAMEMODE = 2
        for i in range(2, PLAYER_COUNT+2):              #top player score used for GAMEMODE = 2
            if PlayerScore[1] < PlayerScore[i]:
                PlayerScore[1] = PlayerScore[i]
                break
        BoardCards[int(ClientInput[0][0])] = BoardCards[0]          #move table card to winner player
        for i in range(1, PLAYER_COUNT+1):                          #rearrange card items to match format
            if i == int(ClientInput[0][0]):
                for j in range(i-1, PLAYER_COUNT):
                    BoardCards[i][j], BoardCards[i][j+1] = BoardCards[i][j+1], BoardCards[i][j] 
            else:
                j = int(ClientInput[0][0])-1 if i > int(ClientInput[0][0]) else int(ClientInput[0][0])-2
                BoardCards[i][j], BoardCards[i][PLAYER_COUNT-1] = BoardCards[i][PLAYER_COUNT-1], BoardCards[i][j]
        GenTableCard()
        ClientInput = []
        #TODO send back info about cards to clients
    else:
        ClientInput.pop(0)



