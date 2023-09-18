'''
Quiz
Autor:Murat-Can
Datum:15.09.23
'''

#lebenspunkte und punkte
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

#---------------------------------------------------------------------------------------#

#Begruessung
print("Hallo und viel Spass bei meinem Quiz! \n\n ")

#---------------------------------------------------------------------------------------#

#Schwierigkeits Auswahl
print("Waehlen die Schwierigkeit aus auf der sie spielen wollen! \n\n\t" 
    "L: Leicht (3 Leben) \n\t" 
    "M: Mittel (2 Leben) \n\t" 
    "S: Schwer (1 Leben) \n\n")

while True:
    input_string = input("Ihre Wahl?: ")
    print('--------------------------------------------------------------')
    difficulty = input_string.lower()

    if difficulty == "l":
        lp += 3
        print(f"\n\n\nSie Haben den leichten Schwierigkeitsgrad gewaehlt. Sie haben {lp} Leben, viel glueck! \n\n\n")
        break
    elif difficulty == "m":
        lp += 2
        print(f"\n\n\nSie Haben den mittleren Schwierigkeitsgrad gewaehlt. Sie haben {lp} Leben, viel glueck! \n\n\n")
        break
    elif difficulty == "s":
        lp += 1
        print(f"\n\n\nSie Haben den schweren Schwierigkeitsgrad gewaehlt. Sie haben {lp} Leben, viel glueck! \n\n\n")
        break
    else:
        print("Ungueltige Eingabe!")

#---------------------------------------------------------------------------------------#

#Fragen
def frage(frage, antw1, antw2, antw3, loesung):

    global points
    global lp

    print(frage + "\n") 
    print(f"Antwort 1: {antw1}")
    print(f"Antwort 2: {antw2}")
    print(f"Antwort 3: {antw3}")
    print('--------------------------------------------------------------')

    antwort = int(input("Welche Antwort ist die Richtige?: "))
    print('--------------------------------------------------------------')
    if antwort == loesung:
        print("\nDas ist Richtig!\n")
        points += 1
        print(f"\nDeine Punktzahl ist nun {points}\n")
        print('--------------------------------------------------------------')
    elif antwort != loesung:
        print("Falsche Antwort!")
        lp -= 1
        print(f"\n\nDeine Punktzahl ist nun {points}\n")
        print('--------------------------------------------------------------')
        print(f"Sie haben nun {lp} Leben")   


while True:
    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage("Frage 1: Wieviel Bit sind in einem Byte?", "4", "16", "8", 3)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage('Was bedeutet der Datentyp \"int\" auf Deutsch', 'Integer', 'Ganzzahl', 'Vollstaendige Zahl', 2)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage("Welches Schlüsselwort wird in Python verwendet, um eine Schleife zu beenden?", "end", "break", "stop", 2)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage("Welche Art von Variable kann nur zwei Werte haben, True oder False?", "Integer", "String", "Boolean", 3)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage("Welches Zeichen wird in den meisten Programmiersprachen verwendet, um einen Kommentar zu markieren?", "#", "//", "*", 1)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage("Welches Python-Modul ermöglicht den Zugriff auf mathematische Funktionen wie Sinus und Quadratwurzel?", "os", "math", "sys", 2)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    frage('Wie heisst die 2te Frau von Henry the 8th', 'Anne Boleyn', 'Catherine Howered', 'Catherine Parr', 1)

    if lp == 0:
        print("\n\nSchade viel Glueck beim naechsten mal!")
        break

    break

print(f'\n\nDu hast {points} Punkte erreicht!\n\nGlueckwunsch!\n\n')
print('--------------------------------------------------------------')


#Highscore abspeichern
if points > highscore:
    print("Herzlichen Glückwunsch! Neuer Highscore erreicht!")
    highscore = points
    with open("Highscore.txt", "w") as highScore:
        highScore.write(str(highscore))
else:
    print("Aktueller Highscore:", highscore)