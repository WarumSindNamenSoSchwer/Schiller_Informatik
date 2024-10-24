from random import randint

class Spiel:
    def __init__(self) -> None:
        self.computer_wahl: int = None
        self.spieler_wahl: int = None
        #   Attribute hinzufügen

    def start(self):
        spieler = Spieler()

        while True: #   es kann eine andere Bedingung gewählt werden
            #   Die Spiellogik kommt hier hin, für die Wahl des Computers wird die Verwendung von randint vorrausgesetzt
            self.computer_wahl = randint(1,3)
            if self.computer_wahl == self.spieler_wahl:
                #   in den folgenden Zeilen soll nur der Input des Spielers mit der zufälligen Wahl des "Computers" verglichen werden
                #   und je nach ausgang soll ein anderes Ereignis ausgeführt werden 
                #   z.B. dem Spieler wird zu einer Variable Siege ein Sieg addiert.
                ...
        
        
        print(self.player_wins, self.computer_wins, self.ties)
        #   Am Ende sollen die Ergebnisse ausgegeben werden dies kann noch verschönert dargestellt werden ;)


class Spieler:
    def __init__(self) -> None:
        self.wahl = None
        self.optionen = {
            1: "Schere",
            2: "Stein",
            3: "Papier",
            4: "Exit"
        }   #   Das Dictionary soll ausgefüllt werden

    def wählen(self) -> int:
        #   Hier trifft der Spieler eine Wahl aus den Optionen, diese Funktion soll den Schlüssel der Wahl wiedergeben
        #   den Schlüssel gibt man mit dem "return" Schlüsselwort wieder
        ...
         
spiel = Spiel()
spiel.start()