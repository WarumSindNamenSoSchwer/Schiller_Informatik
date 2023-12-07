import turtle as t
import hangman_draw as hD
import hangman_Functions as hF

# Lese Wörter aus einer Datei und entferne Leerzeichen
words_list = hF.read_word_from_list("Hangman/words.txt")

while True:
    # Initialisiere verschiedene Listen und Sets für das Spiel
    verschlüsselt = []        # Liste für die verschlüsselte Version des zu ratenden Wortes
    list_wort = []            # Liste für das zu ratende Wort (für Entwicklungs- und Debugging-Zwecke)
    geratene_Buchstaben = set()   # Set für die bereits geratenen Buchstaben

    # Mische die Wörterliste und wähle ein zufälliges Wort aus
    zu_ratendes_wort = hF.shuffle_list_1word(words_list)
    
    # Initialisiere die verschlüsselte Version des Wortes
    hF.encrypt_word(zu_ratendes_wort,verschlüsselt,list_wort,dev_Opt=1)
    
    versuche = 11   # Anzahl der Versuche
    leben = 11      # Anzahl der Leben

    while versuche > 0:
            
        # Überprüfe erneut, ob das Wort bereits komplett geraten wurde
        if hF.check_game_state(verschlüsselt, versuche, True):
            break

        # Benutzereingabe für einen Buchstaben oder das gesamte Wort
        eingabe = t.textinput(verschlüsselt, "Enter a letter or the word, be warned if the whole word is wrong you have lost peasant!\n" +
                              f"You have {versuche} tries")
        eingabe = eingabe.lower()

        # Überprüfe, ob der Buchstabe bereits geraten wurde
        if eingabe in geratene_Buchstaben:
            print("You already guessed that letter. Try again.")
            continue

        geratene_Buchstaben.add(eingabe)
        
        # Überprüfe, ob die Eingabe das gesamte Wort ist und ob es korrekt ist
        if eingabe == zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            print("1")
            # Einzubauendes Easteregg
            hD.easteregg()
            if hF.check_game_state(verschlüsselt, versuche, False):
                break
        # Überprüfe, ob die Eingabe das gesamte Wort ist und ob es falsch ist
        elif eingabe != zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            versuche = 0
            for i in range(leben):
                hD.Hangmandraw(leben)
                leben -=1
            if hF.check_game_state(verschlüsselt, versuche, False, 1):
                break

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

    t.reset()
    t.clear()
    t.ht()

print("Hello World!")