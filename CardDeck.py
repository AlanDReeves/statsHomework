import random

class Card:
    def __init__(self, cardNumber: int):
        self.number = cardNumber

class CardDeck:
    """Simulates a deck of cards for permutation purposes"""
    def __init__(self, numOfCards: int):
        """CardDeck constructor.
        numOfCards - int: the number of cards to put in the deck"""
        self.numCards = numOfCards
        self.deck = []
        for i in range(1, self.numCards + 1):
            temp = Card(i)
            self.deck.append(temp)

    def permute(self) -> list:
        """Returns a pseudo-random permutation of cards as a list. 
        Does not modify the original deck"""
        # copy original deck
        copy = self.deck[:]
        # create copy to return later
        permutation = []
        while len(copy) > 0:
            # select an index from copy at random
            randomIndex = random.randrange(len(copy))
            # remove from copy, place in permutation
            temp = copy[randomIndex]
            copy.remove(copy[randomIndex])
            permutation.append(temp)
        return permutation