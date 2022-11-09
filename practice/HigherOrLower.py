# File: HigherOrLower.py

# HigherOrLower
import random

# Card constants
SUIT_TUPLE = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'King', 'Queen')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop one off the top of the deck 
    # and return
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

print("Welcome to Higher or Lower.")
print("You have to choose whether the next card shown to you will be higher or lower than the current card.")
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print("You have 50 points to start.")
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value':thisValue+1}
        startingDeckList.append(cardDict)

score = 50

while True: # Play multiple games
    print() 
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(startingDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardSuit = currentCardDict['suit']
    currentCardValue = currentCardDict['value']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): # Play one game of this many cards
        answer = input("Will the next card be higher or lower than the " + currentCardRank + ' of ' + currentCardSuit + "? (enter h or l):")
        answer = answer.casefold() # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print("Next card is:", nextCardRank + ' of ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print("You got it right, it was higher!")
                score += 20
            else:
                print("Sorry, it was not higher.")
                score -= 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                print("You got it right, it was lower!")
                score += 20
            else:
                print("Sorry, it was not lower.")
                score -= 15
            
        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue # don't need current suit

    goAgain = input("To play again, press ENTER, or 'q' to quit:")
    if goAgain == 'q':
        break

print("OK bye")