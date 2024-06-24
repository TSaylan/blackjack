class Blackjack:

    players = []

    def __init__(self, players) -> None:
        self.players = players

    def start(self):
        for i in range (len(self.players)):
            print(f"{self.players[i].name}")