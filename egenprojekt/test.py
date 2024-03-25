import random

class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value == 1:
            return 'Ace'
        elif self.value == 10:
            return 'Jack'
        elif self.value == 10:
            return 'Queen'
        elif self.value == 10:
            return 'King'
        else:
            return str(self.value)

class Deck:
    def __init__(self):
        self.cards = [Card(value) for value in range(1, 11)] * 4

    def shuffle(self):
        random.shuffle(self.cards)