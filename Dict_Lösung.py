import turtle

# Aufgabe 1
person = {}

# Aufgabe 2
person["Name"] = "Alice"
person["Alter"] = 30
person["Stadt"] = "Berlin"

# Aufgabe 3
print(person["Alter"])

# Aufgabe 4
if "Geschlecht" not in person:
    person["Geschlecht"] = "weiblich"

# Aufgabe 5
adresse = {
    "Straße": "Hauptstraße 123",
    "PLZ": "12345",
    "Land": "Deutschland"
}
person.update(adresse)

# Aufgabe 6
print(person.keys())

# Aufgabe 7
person.pop("Stadt")

# Überprüfen der Ergebnisse
print(person)

# Aufgabe 8
print("Aufgabe 8:")
for key, value in person.items():
    print(f"{key}: {value}")

# Aufgabe 9
print("\nAufgabe 9:")
while person["Alter"] <= 35:
    print(f"Aktuelles Alter: {person['Alter']}")
    person["Alter"] += 1

# Aufgabe 10
farben_dict = {
    "rot": (1, 0, 0),
    "blau": (0, 0, 1),
    "grün": (0, 1, 0)
}

turtle.speed(2)

for farbe, rgb in farben_dict.items():
    turtle.fillcolor(rgb)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(70)

# Aufgabe 11
bewegungen = {
    "vorwärts": turtle.forward,
    "rückwärts": turtle.backward,
    "links": turtle.left,
    "rechts": turtle.right,
    "w": turtle.forward,
    "s": turtle.backward,
    "a": turtle.left,
    "d": turtle.right
}

while True:
    eingabe = input("Bewegung (vorwärts/d, rückwärts/a, links/w, rechts/s) oder 'exit' zum Beenden: ")
    if eingabe == 'exit':
        break
    elif eingabe in bewegungen:
        bewegungen[eingabe](90)

turtle.done()