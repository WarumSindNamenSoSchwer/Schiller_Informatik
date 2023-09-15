'''
Quiz
Autor:Murat-Can
Datum:15.09.23
'''

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
    difficulty = input_string.lower()

    if difficulty == "l":
        print("Sie Haben den leichten Schwierigkeitsgrad gewaehlt. Sie haben 3 Leben, viel glueck!")
        break
    elif difficulty == "m":
        print("Sie Haben den mittleren Schwierigkeitsgrad gewaehlt. Sie haben 2 Leben, viel glueck!")
        break
    elif difficulty == "s":
        print("Sie Haben den schweren Schwierigkeitsgrad gewaehlt. Sie haben 1 Leben, viel glueck!")
        break
    else:
        print("Ungueltige Eingabe!")

#---------------------------------------------------------------------------------------#


#Fragen

points = 0

while True:
    if ph == -1:
        break

    frage1 = 3
    print("Frage 1: Wieviel Bit sind in einem Byte? \n\t"
          "Antwort 1: 4\n\t"
          "Antwort 2: 16\n\t"
          "Antwort 3: 8\n\n")

    antwort = int(input("Welche Antwort ist die richtige? : "))

    if antwort == frage1:
        print("Das ist Richtig!")
        points += 1
        print(f"Deine Punktzahl ist nun {points}")
