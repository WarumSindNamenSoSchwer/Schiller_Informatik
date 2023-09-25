'''
print("Willkommen zum Quiz")


richtig = 0
falsch = 0





print("Was ist die Bundeshauptstadt?")
print("""
1. Hamburg
2. Berlin
3. Bremen
4. Köln
5. Bonn
""")


richtige_antwort = 1
nutzer_antwort = input("Antwort: ")

if str(richtige_antwort).lower() == str(nutzer_antwort):
	print("Richtig")
	richtig = richtig + 1
else:
	print("Falsch, richtig währe" + str(richtige_antwort))
	falsch = falsch + 1







print("Wie viele Bundesländer gibt es?")
print("Bitte gebe eine Zahl ein.")


richtige_antwort = 16
nutzer_antwort = input("Antwort: ")


if str(richtige_antwort).lower() == str(nutzer_antwort):
	print("Richtig")
	richtig = richtig + 1
else:
	print("Falsch, richtig währe: " + str(richtige_antwort))
	falsch = falsch + 1






print("Was ist dar größte Staat der Welt?")
print("Bitte gebe den Namen des Staates ein")


richtige_antwort = "Russland"
nutzer_antwort = input("Antwort: ")


if str(richtige_antwort).lower() == str(nutzer_antwort):
	print("Richtig")
	richtig = richtig + 1
else:
	print("Falsch, richtig währe: " + str(richtige_antwort))
	falsch = falsch + 1




print("Richtige Antworten: " + str(richtig))
print("Falsche Antworten: " + str(falsch))
print("Punkte: " + str(richtig - falsch)) 



'''

#——————————————————————————————————————————————————————————————————————————


Leben = 3
print ("Leben =", Leben)
print (" ")

name = input ("wie weißt du?: ")
print ("Hallo",name,". Good Luck.")


while Leben >= 0:
    ##is the player ready to start
    play = input ("wills du starten? (Tippe J für ja und N für N): ")
    if play == "j" or play == "j":
        from time import sleep
        sleep (1.0)
        print("es geht los in...")
        sleep (1.0)
        print("3")
        sleep(1.0)
        print("2")
        sleep(1.0)
        print("1")
        sleep(1.0)
    ##3, 2, 1 countdown added wk.4 friday
    elif play == "N" or play == "n":
        print ("Ende")
        break
    else:
        print ("Das ist keine richtige Angabe.\n")

    print("\n")

    ## 1st Question
    question1 = "1. Wer hat die Letzte Basketball Weltmeisterschaft gewonnen?"
    options1 = " a. Deutschland \n b. USA \n c. Serbien \n d. Spanien"
    print (question1)
    print (options1)
    answer = input ("> ")
    if answer == "A" or answer == "a":
        print ("Correct!")
    else:
        print("Incorrect.")
        print ("Leben =", Leben - 1)
        Leben=Leben-1
        if Leben == 0:
            break


    ## 2nd Question
    question2 = "2. Wer ist zweiter Platz geworden"
    options2 = " a. USA \n b. Serbien \n c. Kanada \n d. Spanien"
    print (question2)
    print (options2)
    answer = input ("> ")
    if answer == "D" or answer == "d":
        print ("Correct!")
    else:
        print("Incorrect.")
        print("Leben =", Leben - 1)
        Leben=Leben-1
        if Leben == 0:
            break

    ## 3rd Question
    question3 ="3. Wie viele Spieler spielen auf dem Feld?(pro Team)"
    options3 =" a. 6 \n b. 4 \n c. 10\n d. 5"
    print (question3)
    print (options3)
    answer = input ("> ")
    if answer == "D" or answer == "d":
        print ("Correct!")
    else:
        print("Incorrect.")
        print ("Leben =", Leben - 1)
        Leben=Leben-1
        if Leben == 0:
            break


    ## 4th Question
    question4 = "4. Wie war das Endergebnis bei Deutschland gegen Serbien?"
    options4 = " a. 101/70 \n b. 83/77 \n c. 90/110\n d. 89/93"
    print (question4)
    print (options4)
    answer = input ("> ")
    if answer == "B" or answer == "b":
        print ("Correct!")
    else:
        print("Incorrect.")
        print ("Leben =", Leben - 1)
        Leben=Leben-1
        if Leben == 0:
            break
    
    break