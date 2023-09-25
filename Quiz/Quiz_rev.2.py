#Autor: Murat - Can
#Quiz_rev.2
#Datum: stand rev 2 19.09.23

# Initialisierung von Lebenspunkten und Punkten
lp = 0
points = 0

try:
    with open("Highscore.txt", "r") as highScore:
        highscore_str = highScore.read().strip()
        if highscore_str:
            highscore = int(highscore_str)
        else:
            highscore = 0
except FileNotFoundError:
    highscore = 0

# Schwierigkeitsauswahl und Anzahl der Lebenspunkte festlegen
def choose_difficulty():
    global lp
    print("Waehlen Sie die Schwierigkeit aus, auf der Sie spielen moechten:")
    print("L: Leicht (3 Leben)")
    print("M: Mittel (2 Leben)")
    print("S: Schwer (1 Leben)")

    while True:
        input_string = input("Ihre Wahl?: ").lower()
        if input_string in ["l", "m", "s"]:
            lp = 3 if input_string == "l" else (2 if input_string == "m" else 1)
            print(f"\nSie haben den Schwierigkeitsgrad '{input_string}' gewaehlt. Sie haben {lp} Leben. Viel Glueck!\n")
            break
        else:
            print("Ungueltige Eingabe!")

# Funktion zur Überprüfung und Aktualisierung der Lebenspunkte
def check_lives():
    global lp
    if lp == 0:
        print("\nSchade, viel Glueck beim naechsten Mal!")
        return False
    else:
        print(f"\nDeine Punktzahl ist nun {points}")
        print(f"Sie haben noch {lp} Leben")
        return True

# Fragenfunktion
def frage(fNr, frage, antw1, antw2, antw3, loesung):
    global points
    global lp

    print(f"Frage {fNr}: " + frage + "\n")
    print(f"Antwort 1: {antw1}")
    print(f"Antwort 2: {antw2}")
    print(f"Antwort 3: {antw3}")

    while True:
        antwort = input("Welche Antwort ist die Richtige?: ")
        if not antwort.isdigit():
            print("Ungueltige Antwort!")
        else:
            if int(antwort) == loesung:
                print("\nDas ist Richtig!\n")
                points += 1
                break
            else:
                print("Falsche Antwort!")
                lp -= 1
                break
    return check_lives()

# Hauptspiel-Loop
def main():
    global points
    global highscore

    # Begrüßung und Schwierigkeitsauswahl
    print("Hallo und viel Spass bei meinem Quiz!\n")
    choose_difficulty()

    # Fragen
    while True:
        if not frage(1 ,"Wie viel Bit sind in einem Byte?", "4", "16", "8", 3):
            break

        if not frage(2 ,'Was bedeutet der Datentyp "int" auf Deutsch?', 'Integer', 'Ganzzahl', 'Vollstaendige Zahl', 2):
            break

        if not frage(3 ,"Welches Schluesselwort wird in Python verwendet, um eine Schleife zu beenden?", "end", "break", "stop", 2):
            break

        if not frage(4 ,"Welche Art von Variable kann nur zwei Werte haben, True oder False?", "Integer", "String", "Boolean", 3):
            break

        if not frage(5 ,"Welches Zeichen wird in den meisten Programmiersprachen verwendet, um einen Kommentar zu markieren?", "#", "//", "*", 1):
            break

        if not frage(6 ,"Welches Python-Modul ermoeglicht den Zugriff auf mathematische Funktionen wie Sinus und Quadratwurzel?", "os", "math", "sys", 2):
            break

        if not frage(7 ,'Wie heißt die 2te Frau von Henry the 8th', 'Anne Boleyn', 'Catherine Howered', 'Catherine Parr', 1):
            break

        break

    # Spielende
    print(f'\n\nDu hast {points} Punkte erreicht!\n\n')
    print('--------------------------------------------------------------')

    # Highscore speichern
    if points > highscore:
        print("Herzlichen Glückwunsch! Neuer Highscore erreicht!")
        highscore = points
        with open("Highscore.txt", "w") as highScore:
            highScore.write(str(highscore))
    else:
        print("Aktueller Highscore:", highscore)

# Das Spiel starten
if __name__ == "__main__":
    main()