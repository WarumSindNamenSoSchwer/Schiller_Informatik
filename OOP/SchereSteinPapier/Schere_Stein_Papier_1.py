from random import randint

class Spiel:
    def __init__(self) -> None:
        #   Attribute hinzufügen

    def start(self):
        spieler = Spieler()

        #   Die Spiellogik kommt hier hin, für die Wahl des Computers wird die Verwendung von randint vorrausgesetzt
        #   Jeder mögliche Ausgang soll ein anderes Ereignis auslösen
        
        print(self.player_wins, self.computer_wins, self.ties)
        #   Am Ende sollen die Ergebnisse ausgegeben werden dies kann noch verschönert dargestellt werden ;)


class Spieler:
    def __init__(self) -> None:
        self.wahl = None
        self.optionen = {}   #   Das Dictionary soll ausgefüllt werden

    def wählen(self) -> int:
        #   Hier trifft der Spieler eine Wahl aus den Optionen, diese Funktion soll den Schlüssel der Wahl wiedergeben
        ...
         
spiel = Spiel()
spiel.start()