#Schere Stein Papier
#murat

from random import randint

class Game:
    def __init__(self) -> None:
        self.player_wins: int = 0
        self.computer_wins: int = 0
        self.ties: int = 0
        self.computer_choice: int = None
        self.player_choice: int = None
        self.round_counter: int = 0

    def start(self):
        player = Player()
        player.player_name()

        while self.player_choice is not 4:
            if self.round_counter == 3:
                print("Want to play another round?")
                choice: str = input(": ")
                if choice.lower() in ("yes", "y", "1"):
                    self.round_counter = 0
                else:
                    break
            self.computer_choice = randint(1,3)
            self.player_choice = player.choose()
            if self.computer_choice == self.player_choice:
                print("Unentschieden...")
                self.ties += 1
                self.round_counter += 1
            elif (self.player_choice == 1 and self.computer_choice == 2) or \
                 (self.player_choice == 2 and self.computer_choice == 3) or \
                 (self.player_choice == 3 and self.computer_choice == 1):
                print("Du hast verloren...")
                self.computer_wins += 1
                self.round_counter += 1
            elif (self.player_choice == 2 and self.computer_choice == 1) or \
                 (self.player_choice == 3 and self.computer_choice == 2) or \
                 (self.player_choice == 1 and self.computer_choice == 3):
                print("Du hast gewonnen!")
                self.player_wins += 1
                self.round_counter += 1
            else:
                print("Exiting Game")
                break
        
        print(" Spieler:" ,self.player_wins, "\n", "Computer:", self.computer_wins, "\n", "Unentschieden:", self.ties)


class Player:
    def __init__(self) -> None:
        self.name = ""
        self.choice = None
        self.options = {
            1: ("schere", "Schere", "Scissors", "scissors", "1"),
            2: ("stein", "Stein", "Rock", "rock", "2"),
            3: ("papier", "Papier", "Paper", "paper", "3"),
            4: ("exit", "Exit", "quit", "Quit", "q", "Q", "4")
        }

    def player_name(self) -> str:
        self.name = input("Wie heißt du?: ")
        return self.name 

    def choose(self) -> int:
        self.choice = input("Triff eine wahl zwischen Schere, Stein, Papier oder exit: ")
        for key in self.options:
            if self.choice in self.options[key]:
                return key




def main() -> None:
    game = Game()
    game.start()

if __name__ == "__main__":
    main()