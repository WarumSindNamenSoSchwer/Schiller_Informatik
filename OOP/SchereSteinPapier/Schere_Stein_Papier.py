from random import randint

class Game:
    def __init__(self) -> None:
        #   Attribute hinzufügen

    def start(self):
        player = Player()
        player.player_name()

        
        #   Die Spiellogik kommt hier hin, für die Wahl des Computers wird die Verwendung von randint vorrausgesetzt
        
        
        print(" Spieler:" ,self.player_wins, "\n", "Computer:", self.computer_wins, "\n", "Unentschieden:", self.ties)


class Player:
    def __init__(self) -> None:
        self.name = ""
        self.choice = None
        self.options = {}   #   Das Dictionary soll ausgefüllt werden

    def player_name(self) -> str:
        #Code...

    def choose(self) -> int:
        #Code...
        
game = Game()
game.start()