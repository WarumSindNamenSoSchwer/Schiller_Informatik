import turtle as t
import random
import hangmandraw as hD

with open("tests/words.txt") as f:
    words = f.readlines()
    words = [x.strip() for x in words]



verschlüsselt = []
list_wort = []   #dev
geratene_Buchstaben = []

istAn = True
while istAn:
    random.shuffle(words)
    zu_ratendes_wort = words[0]
    zu_ratendes_wort.split(',')
    
    for index in zu_ratendes_wort:
        verschlüsselt.append('_')
        list_wort.append(index) #dev

    #Dev
    print(zu_ratendes_wort)
    print(list_wort)
    print(verschlüsselt)
    
    versuche = 11
    leben = 11
    
    while versuche > 0:

        eingabe = t.textinput(verschlüsselt, "Enter a letter or the word, be warned if the whole word is wrong you have lost peasant!")
        eingabe = eingabe.lower()
        
        if eingabe == zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            print("1")
            #einzubauendes easteregg
            hD.easteregg()
            replay = t.textinput("You lost Dumbo", "Wanna Play again? Yes/No")
            if replay.lower() == "yes" or replay.lower() == "y":
                versuche = 11
                leben = 11
                print(versuche)
                break
        elif eingabe != zu_ratendes_wort and eingabe.isalpha() and len(eingabe) == len(zu_ratendes_wort):
            versuche -= versuche
            for i in range(leben):
                #function call draw hangman(Leben)
                hD.Hangmandraw(leben)
                pass
            replay = t.textinput("You lost Dumbo", "Wanna Play again? Yes/No")
            if replay.lower() == "yes" or replay.lower() == "y":
                versuche = 11
                leben = 11
                print(versuche)
                break
        
        for i in range(len(list_wort)):
            if eingabe == list_wort[i] and eingabe.isalpha():
                verschlüsselt[i] = eingabe
                print("1")
                versuche -= 1
                print(versuche)
                break
            elif eingabe != list_wort[i] and eingabe.isalpha():
                leben -= 1
                versuche -=1
                #function call draw hangman(Leben)
                hD.Hangmandraw(leben)
                print(versuche)
                break

