#Aufgabe: Frag den Benutzer nach dem Namen und dessen Noten, errechne anschließend den Durchschnitt.
#Autor: Murat-Can Meric
#Erstellt am 05.09.23

name=input("Gib deinen Namen ein: ")
print("Dein Name ist: "+ name+".")

#Erfasst die Noten
input_string=input("Gib deine Noten mit einem Leerzeichen unterteilt ein: ")
print("Du hast, " + input_string, "eingegeben.")

#String wird an den leerzeichen aufgeteilt und in einer Liste gespeichert
grades= input_string.split()

#Setzt jedes Element in der liste auf Typ Float
for i in range(len(grades)):
    grades[i]=float(grades[i])

#Berechnecht den Durchschnitt mit der Summe der Elemente und teilt diese durch die Länge der Liste
average_grade=sum(grades) / len(grades)

#Ausgabe des Durchschnitts
print("Durchschnitt = "+ str(average_grade))

if average_grade < 2.5:
    print("Du bist ein guter Schüler!")
elif 2.5 < average_grade < 4.0:
    print("Weiter so es ist noch luft nach oben!")
elif 4.0 < average_grade < 6.0:
    print("Vielleicht wirds nächstes mal besser!")

for i in range(3):   
    if i == 2:
        print("Danke fürs nutzen dieser App.")
    else:
        print("\n")