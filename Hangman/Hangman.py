import random
import turtle as t


t.setup(1.0, 1.0)
#Kreierung vom Wort
with open("Hangman/wortliste.txt") as f:
    words = f.readlines()
    words = [x.strip() for x in words]

random.shuffle(words)

wort = words[0]
print(wort)

#Bestimmen der länge des Wortes
wortlänge = len(wort)
print(wortlänge)

#Zeichnen der Striche
t.penup()
if wortlänge > 15:
    t.goto(-800,-400)
elif wortlänge > 8:
    t.goto(-500,-400)
else:
    t.goto(-300,-400)
for index in range(wortlänge):
    t.pendown()
    t.forward(50)
    t.penup()
    t.forward(25)

eingabe = t.textinput("Buchstaben eingeben", "Bitte gib einen Buchstaben ein.")

if eingabe in wort:
    print(1)
else:
    print(2)
