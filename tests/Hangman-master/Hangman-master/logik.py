import turtle as t
import random
import hangmandraw as hD
import self_destruct as sD

with open("Hangman/words.txt") as f:
    words = f.readlines()
    words = [x.strip() for x in words]

verschlüsselt = []
list_wort = []   #dev
geratene_Buchstaben = set()

istAn = True
while istAn:
    random.shuffle(words)
    zu_ratendes_wort = words[0]
    
    for index in zu_ratendes_wort:
        verschlüsselt.append('_')
        list_wort.append(index) #dev

    
    print(zu_ratendes_wort) #Dev
    print(list_wort) #Dev
    print(verschlüsselt) #Dev
    
    versuche = 11
    leben = 11
    
    while versuche > 0:
        
        for i in range(len(verschlüsselt)):
            if "_" not in verschlüsselt:
                replay = t.textinput("You won somehow", "Wanna Play again? Yes/No")
                if replay.lower() == "yes" or replay.lower() == "y":
                    versuche = 11
                    leben = 11
                    
                    verschlüsselt = []
                    list_wort = []   #dev
                    geratene_Buchstaben = set()

                    print(versuche) #Dev
                    break
                else:
                    sD.self_destruct()

        eingabe = t.textinput(verschlüsselt, "Enter a letter or the word, be warned if the whole word is wrong you have lost peasant!\n"+
        f"You have {versuche} tries")
        eingabe = eingabe.lower()

        if eingabe in geratene_Buchstaben:
            print("You already guessed that letter. Try again.")
            continue

        geratene_Buchstaben.add(eingabe)
        
        for i in range(len(verschlüsselt)):
            if "_" not in verschlüsselt:
                replay = t.textinput("You won somehow", "Wanna Play again? Yes/No")
                if replay.lower() == "yes" or replay.lower() == "y":
                    versuche = 11
                    leben = 11

                    verschlüsselt = []
                    list_wort = []   #dev
                    geratene_Buchstaben = set()

                    print(versuche) #Dev
                    break
                else:
                    sD.self_destruct()

        if eingabe == zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            print("1")
            #einzubauendes easteregg
            hD.easteregg()
            replay = t.textinput("You won somehow", "Wanna Play again? Yes/No")
            if replay.lower() == "yes" or replay.lower() == "y":
                versuche = 11
                leben = 11

                verschlüsselt = []
                list_wort = []   #dev
                geratene_Buchstaben = set()

                print(versuche) #Dev
                break
            else:
                sD.self_destruct()
        elif eingabe != zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            versuche = 0
            for i in range(leben):
                hD.Hangmandraw(leben)
            replay = t.textinput("You lost Dumbo", "Wanna Play again? Yes/No")
            if replay.lower() == "yes" or replay.lower() == "y":
                versuche = 11
                leben = 11
                print(versuche) #Dev
                break
            else:
                sD.self_destruct()

        if len(eingabe) != len(zu_ratendes_wort) and eingabe.isalpha():
            for i in range(len(zu_ratendes_wort)):
                if zu_ratendes_wort[i] in eingabe and verschlüsselt[i] == "_":
                    verschlüsselt[i] = zu_ratendes_wort[i]
                    print("1")  # Dev
                    print(versuche)  # Dev
            versuche -= 1
            if eingabe not in zu_ratendes_wort and eingabe.isalpha() and eingabe != " " and len(eingabe) > 1:
                for i in range(len(eingabe)):
                    leben -= 1
                    hD.Hangmandraw(leben)
                versuche -= 1
        
        for i in range(len(list_wort)):
            if eingabe == list_wort[i] and eingabe.isalpha() and verschlüsselt[i] == "_" and eingabe != " ":
                verschlüsselt[i] = eingabe
                print("1")  # Dev
                print(versuche)  # Dev

        if eingabe not in list_wort and eingabe.isalpha() and eingabe != " " and len(eingabe) == 1:
            leben -= 1
            versuche -= 1
            hD.Hangmandraw(leben)

