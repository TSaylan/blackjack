import random

class Blackjack:

    players = []

    suits = ['♥', '♦', '♠', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([suit, rank])

    def __init__(self, players) -> None:
        self.players = players

    def start(self):
        print("\n")
        for i in range (len(self.players)):
            for _ in range(2):
                card = self.deck.pop(self.deck.index(random.choice(self.deck)))
                self.players[i].cards.append(card)
            print(f"{self.players[i].name} >> {self.players[i].cards}")
        print("\nDealer\n\n")