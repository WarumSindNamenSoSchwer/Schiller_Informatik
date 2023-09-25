'''
hauptstadt Deutschland
wie viele bezirke hat Berlin
wie viele einwohner hat Berlin
'''

#Autor: Jara
#Datum: 23.09.23
#Thema: Quiz mit while Schleife


name = input('Hallo wie heißt du?: ')
print(f'Hallo {name} und viel spaß bei meinem Quiz!\n')

print('Du hast drei Versuche pro Frage.\nWenn du beim ersten Versuch die richtige Antwort angibst dann bekommst du 3 Punkte,\nbeim Zweiten 2 Punkte und beim Dritten nur 1 Punkt.')

while True:
    versuche = 3
    punkte = 0

    #frage zur hauptstadt deutschlands
    antwort1 = 'Berlin'
    print('Was ist die Hauptstadt Deutschlands?:\n\ta) Köln\n\tb) Berlin\n\tc) NRW')
    

    while True:
        if versuche == 0:
            break
        antwort = input('Antwort: ')

        if antwort.lower() == 'berlin' or antwort.lower() == 'b':
            if versuche == 3:
                punkte += 3
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
            elif versuche == 2:
                punkte += 2
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
            elif versuche == 1:
                punkte += 1
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
        elif antwort.lower() == 'köln' or antwort.lower() == 'a' or antwort.lower() == 'c' or antwort.lower() == 'nrw':
            versuche -= 1
            if versuche == 0:
                print('Schade viel Glück bei der nächsten Frage!')
                continue
            print(f'Das war leider Falsch du hast noch {versuche} Versuche.')
        else:
            print('Ungültige Eingabe!')



    #frage zur anzahl der bezirke in berlin
    antwort2 = '12'
    print('Wie viele Bezirke hat Berlin?:\n\ta) 6\n\tb) 22\n\tc) 12')
    

    while True:
        if versuche == 0:
            break
        antwort = input('Antwort: ')

        if antwort.lower() == '12' or antwort.lower() == 'c':
            if versuche == 3:
                punkte += 3
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
            elif versuche == 2:
                punkte += 2
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
            elif versuche == 1:
                punkte += 1
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
        elif antwort.lower() == 'b' or antwort.lower() == 'a' or antwort.lower() == '6' or antwort.lower() == '22':
            versuche -= 1
            if versuche == 0:
                print('Schade viel Glück bei der nächsten Frage!')
                continue
            print(f'Das war leider Falsch du hast noch {versuche} Versuche.')
        else:
            print('Ungültige Eingabe!')

    
    #frage zur anzahl der anwohner in berlin
    antwort2 = '3,6 Mio'
    print('Wie viele Anwohner (grob geschätzt) hat Berlin?:\n\ta) 3,6 Mio.\n\tb) 2,5 Mio\n\tc) 6 Mio')
    

    while True:
        if versuche == 0:
            break
        antwort = input('Antwort: ')

        if antwort.lower() == '3.6 Mio' or antwort.lower() == 'a' or antwort.lower() == '3,6Mio':
            if versuche == 3:
                punkte += 3
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
            elif versuche == 2:
                punkte += 2
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
            elif versuche == 1:
                punkte += 1
                print(f'Glückwunsch du hast {punkte} Punkte')
                break
        elif antwort.lower() == 'b' or antwort.lower() == 'c' or antwort.lower() == '2,5 Mio' or antwort.lower() == '6 Mio' or antwort.lower() == '6Mio' or antwort.lower() == '2,5Mio':
            versuche -= 1
            if versuche == 0:
                print('Schade viel Glück bei der nächsten Frage!')
                continue
            print(f'Das war leider Falsch du hast noch {versuche} Versuche.')
        else:
            print('Ungültige Eingabe!')

    #Um das Programm zu beenden.
    break