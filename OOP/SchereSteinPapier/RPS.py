from random import randint

class Game:
    def __init__(self) -> None:
        self.gametype: int = None #Game type 1 = Singleplayer, 2 = Multiplayer

        self.player1_wins: int = 0 #Multiplayer
        self.player2_wins: int = 0 #Multiplayer

        self.computer_wins: int = 0 #Singelplayer
        self.player_wins: int = 0 #Singelplayer

        self.options = randint(1, 3) #Random number for the options

    def ergebnis(self) -> None:#formatting can be imporved
        if self.gametype == 2:
            print(f"Spieler 1 hat {self.player1_wins} gewonnen!")
            print(f"Spieler 2 hat {self.player2_wins} gewonnen!")
        else:
            print(f"Du hast {self.player_wins} gewonnen!")
            print(f"Der Computer hat {self.computer_wins} gewonnen!")

    def multiplayer(self) -> None:
        name1 = input("Wie heißt du Spieler 1?: ")
        player1 = Player("Spieler 1")

        name2 = input("Wie heißt du Spieler 2?: ")
        player2 = Player("Spieler 2")

        while True:
            p1_choice = player1.choose()
            p2_choice = player2.choose()

            if p1_choice == p2_choice:
                print("Unentschieden!")
            elif (p1_choice == 2 and p2_choice == 1) or (p1_choice == 1 and p2_choice == 3) or (p1_choice == 3 and p2_choice == 2):
                print("Spieler 1 gewinnt!")
                self.player1_wins += 1
            elif (p1_choice == 1 and p2_choice == 2) or (p1_choice == 2 and p2_choice == 3) or (p1_choice == 3 and p2_choice == 1):
                print("Spieler 2 gewinnt!")
                self.player2_wins += 1
            elif p1_choice == 4 or p2_choice == 4:
                print("Du hast das Spiel verlassen!\n")
                self.ergebnis()
                break

    def singleplayer(self) -> None:

        computer = self.options
        #print(f"Computer: {computer}")#dev

        name = input("Wie heißt du?: ")
        player = Player(name)

        while True:
            p_choice = player.choose()
            if p_choice == computer:
                print("Unentschieden")
            elif p_choice == 2 and computer == 1 or p_choice == 1 and computer == 3 or p_choice == 3 and computer == 2:
                print("Du hast gewonnen!")
                self.player_wins += 1
            elif p_choice == 1 and computer == 2 or p_choice == 2 and computer == 3 or p_choice == 3 and computer == 1:
                print("Du hast verloren!")
                self.computer_wins += 1
            elif p_choice == 4:
                print("Du hast das Spiel verlassen!\n")
                Game.ergebnis(self)
                break

    def choose_gametype(self) -> None:
        #add while true for type checking + if statement for quit
        self.gametype = int(input("Welchen Spielmodus möchtest du spielen?\n\t1. Singleplayer\n\t2. Multiplayer\n\t3. Beenden\n"))
        if self.gametype == 1:
            Game.singleplayer(self)
        elif self.gametype == 2:
            print("Multiplayer doesnt really make sense")
            Game.multiplayer(self)
        elif self.gametype == 3:
            print("Du hast das Spiel verlassen!")
            Game.ergebnis(self)


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.choice = None
        self.options = {
            1: ("stein", "Stein", "Rock", "rock", "1"),
            2: ("papier", "Papier", "Paper", "paper", "2"),
            3: ("schere", "Schere", "Scissors", "scissors", "3"),
            4: ("exit", "Exit", "quit", "Quit", "q", "Q", "4")
        }

    def choose(self) -> int:
        #add while true for type checking

        self.choice = input(f"{self.name}, wähle eine Option: \n\tStein, \n\tPapier, \n\tSchere, \n\tExit \nDeine Wahl: ")
        print(f"{self.name} hat {self.choice} gewählt.")

        for key, value in self.options.items():
            if self.choice in value:
                return key

g = Game()
g.choose_gametype()