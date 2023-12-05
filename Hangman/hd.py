import turtle as t
import random
import hangmandraw as hD
import self_destruct as sD

# Lese Wörter aus einer Datei und entferne Leerzeichen
with open("Hangman/words.txt") as f:
    words = f.readlines()
    words = [x.strip() for x in words]

# Initialisiere verschiedene Listen und Sets für das Spiel
verschlüsselt = []        # Liste für die verschlüsselte Version des zu ratenden Wortes
list_wort = []            # Liste für das zu ratende Wort (für Entwicklungs- und Debugging-Zwecke)
geratene_Buchstaben = set()   # Set für die bereits geratenen Buchstaben

istAn = True
while istAn:
    # Mische die Wörterliste und wähle ein zufälliges Wort aus
    random.shuffle(words)
    zu_ratendes_wort = words[0]
    
    # Initialisiere die verschlüsselte Version des Wortes
    for index in zu_ratendes_wort:
        verschlüsselt.append('_')
        list_wort.append(index)  # Entwicklungs- und Debugging-Zwecke

    print(zu_ratendes_wort)   # Debug-Ausgabe
    print(list_wort)          # Debug-Ausgabe
    print(verschlüsselt)      # Debug-Ausgabe
    
    versuche = 11   # Anzahl der Versuche
    leben = 11      # Anzahl der Leben

    while versuche > 0:
        # Überprüfe, ob das Wort bereits komplett geraten wurde
        for i in range(len(verschlüsselt)):
            if "_" not in verschlüsselt:
                replay = t.textinput("You won somehow", "Wanna Play again? Yes/No")
                if replay.lower() == "yes" or replay.lower() == "y":
                    versuche = 11
                    leben = 11
                    verschlüsselt = []
                    list_wort = []   # Entwicklungs- und Debugging-Zwecke
                    geratene_Buchstaben = set()
                    print(versuche)  # Debug-Ausgabe
                    break
                else:
                    sD.self_destruct()

        # Benutzereingabe für einen Buchstaben oder das gesamte Wort
        eingabe = t.textinput(verschlüsselt, "Enter a letter or the word, be warned if the whole word is wrong you have lost peasant!\n" +
                              f"You have {versuche} tries")
        eingabe = eingabe.lower()

        # Überprüfe, ob der Buchstabe bereits geraten wurde
        if eingabe in geratene_Buchstaben:
            print("You already guessed that letter. Try again.")
            continue

        geratene_Buchstaben.add(eingabe)
        
        # Überprüfe erneut, ob das Wort bereits komplett geraten wurde
        for i in range(len(verschlüsselt)):
            if "_" not in verschlüsselt:
                replay = t.textinput("You won somehow", "Wanna Play again? Yes/No")
                if replay.lower() == "yes" or replay.lower() == "y":
                    versuche = 11
                    leben = 11
                    verschlüsselt = []
                    list_wort = []   # Entwicklungs- und Debugging-Zwecke
                    geratene_Buchstaben = set()
                    print(versuche)  # Debug-Ausgabe
                    break
                else:
                    sD.self_destruct()

        # Überprüfe, ob die Eingabe das gesamte Wort ist und ob es korrekt ist
        if eingabe == zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            print("1")
            # Einzubauendes Easteregg
            hD.easteregg()
            replay = t.textinput("You won somehow", "Wanna Play again? Yes/No")
            if replay.lower() == "yes" or replay.lower() == "y":
                versuche = 11
                leben = 11
                verschlüsselt = []
                list_wort = []   # Entwicklungs- und Debugging-Zwecke
                geratene_Buchstaben = set()
                print(versuche)  # Debug-Ausgabe
                break
            else:
                sD.self_destruct()
        # Überprüfe, ob die Eingabe das gesamte Wort ist und ob es falsch ist
        elif eingabe != zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            versuche = 0
            for i in range(leben):
                hD.Hangmandraw(leben)
            replay = t.textinput("You lost Dumbo", "Wanna Play again? Yes/No")
            if replay.lower() == "yes" or replay.lower() == "y":
                versuche = 11
                leben = 11
                print(versuche)  # Debug-Ausgabe
                break
            else:
                sD.self_destruct()

        # Überprüfe, ob die Eingabe die richtige Länge hat und ein Buchstabe ist
        if len(eingabe) != len(zu_ratendes_wort) and eingabe.isalpha():
            for i in range(len(zu_ratendes_wort)):
                # Überprüfe, ob der Buchstabe in der Eingabe vorhanden ist und ob er noch nicht geraten wurde
                if zu_ratendes_wort[i] in eingabe and verschlüsselt[i] == "_":
                    verschlüsselt[i] = zu_ratendes_wort[i]
                    print("1")  # Debug-Ausgabe
                    print(versuche)  # Debug-Ausgabe
            versuche -= 1
            # Überprüfe, ob die Eingabe nicht im zu ratenden Wort ist und ob es sich um einen einzelnen Buchstaben handelt
            if eingabe not in zu_ratendes_wort and eingabe.isalpha() and eingabe != " " and len(eingabe) > 1:
                for i in range(len(eingabe)):
                    leben -= 1
                    hD.Hangmandraw(leben)
                versuche -= 1
        
        # Überprüfe, ob der Buchstabe in der Liste des zu ratenden Wortes vorhanden ist
        for i in range(len(list_wort)):
            if eingabe == list_wort[i] and eingabe.isalpha() and verschlüsselt[i] == "_" and eingabe != " ":
                verschlüsselt[i] = eingabe
                print("1")  # Debug-Ausgabe
                print(versuche)  # Debug-Ausgabe

        # Überprüfe, ob der Buchstabe nicht im zu ratenden Wort ist und ob
        if eingabe not in list_wort and eingabe.isalpha() and eingabe != " " and len(eingabe) == 1:
            leben -= 1
            versuche -= 1
            hD.Hangmandraw(leben)