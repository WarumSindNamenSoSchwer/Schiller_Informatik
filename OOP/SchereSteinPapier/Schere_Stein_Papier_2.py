from random import randint

class Spiel:
    def __init__(self) -> None:
        ...

    def start(self):
        spieler = Spieler()
        ...


class Spieler:
    def __init__(self) -> None:
        ...

    def wählen(self) -> int:
        ...

#   Überlegt mal wofür ich Das hier unten hinzugefügt habe, versucht möglichst nicht zu googlen 
def main() -> None:
    spiel = Spiel()
    spiel.start()

if __name__ == "__main__":
    main()