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
        
        
#Benutzer zur Eingabe des ersten Punktes auffordern
punkt1 = input("Gib den ersten Punkt ein (x1, y1): ")

# Benutzer zur Eingabe des zweiten Punktes auffordern
punkt2 = input("Gib den zweiten Punkt ein (x2, y2): ")

# Verwenden Sie die eval() Funktion, um die eingegebenen Werte in Tupeln zu konvertieren
x1, y1 = eval(punkt1)
x2, y2 = eval(punkt2)

# Berechnung der mittleren Änderungsrate
aenderungsrate = (y2 - y1) / (x2 - x1)

# Ausgabe der Ergebnisse
print("Mittlere Änderungsrate zwischen den Punkten:", aenderungsrate)