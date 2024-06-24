import blackjack

from gamblers.chad import Chad
from gamblers.dave import Dave
from gamblers.mike import Mike
from gamblers.greg import Greg
from gamblers.gary import Gary

game = blackjack.Blackjack

game.players = [Chad, Dave, Mike, Greg, Gary]

blackjack.Blackjack.start(game)