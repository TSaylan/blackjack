import random

class Card:
    def __init__(self, rank, suit, value, open) -> None:
        self.rank = rank
        self.suit = suit
        self.value = value
        self.open = open

    def getFString(Card):
        reset = "\033[0m"
        red = "\033[38;2;255;0;0m"
        black = "\033[38;2;20;20;20m"
        openc = "\033[48;2;240;240;240m"
        closedc = "\033[48;2;120;120;120m"

        text = ""
        background = ""

        if Card.suit in ('♥', '♦'):
            text = red
        elif Card.suit in ('♣', '♠'):
            text = black

        if Card.open == False:
            background = closedc
        else:
            background = openc

        return f"{text}{background} {Card.suit} {Card.rank} {reset}"
    
    def getHandFORMATTEDSTRING(player):
        hand = ""
        for card in player.cards:
            hand += Card.getFString(card) + " "
        return hand.strip()

    def getValue(rank):
        if rank in ('J', 'Q', 'K'):
            value = 10
        elif rank == 'A':
            value = 'A'
        else:
            value = rank
        return value
    
    def  getHandValue(hand):
        aces = 0
        value = 0
        for i in range(len(hand)):
            if hand[i].value == 'A':
                aces += 1
            else:
                value += hand[i].value

        for i in range (aces):
            if value <= 10:
                value += 11
            else: 
                value += 1

        return value

class Blackjack:

    players = []

    suits = ['♥', '♦', '♠', '♣']
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit, Card.getValue(rank), True))

    def __init__(self, players) -> None:
        self.players = players

    def start(self):
        print("\n")
        for i in range (len(self.players)):
            for _ in range(2):
                card = self.deck.pop(self.deck.index(random.choice(self.deck)))
                self.players[i].cards.append(card)
            print(f"{self.players[i].name} >> {Card.getHandFORMATTEDSTRING(self.players[i])} {Card.getHandValue(self.players[i].cards)}")
        print("\nDealer\n\n")


