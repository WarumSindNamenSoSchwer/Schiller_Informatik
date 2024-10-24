import turtle as t

#Aufgabe 1
seiten = 0
while seiten < 4:
	t.forward(100)
	t.right(90)
	seiten += 1

#Aufgabe 2
seiten = 0
while seiten < 3:
	t.forward(100)
	t.left(120)
	seiten += 1

#Aufgabe 3
t.fillcolor("yellow")
t.begin_fill()

seiten = 0
while seiten < 2:
	t.forward(200)
	t.right(90)
	t.forward(100)
	t.right(90)
	seiten += 1

t.end_fill()
t.pencolor("blue")

seiten = 0
while seiten < 2:
	t.forward(200)
	t.right(90)
	t.forward(100)
	t.right(90)
	seiten += 1

#Aufgabe 4
# Haus zeichnen
t.fillcolor("red")
t.begin_fill()
seiten = 0
while seiten < 4:
	t.forward(150)
	t.left(90)
	seiten += 1
t.end_fill()

# Tür zeichnen
t.penup()
t.goto(60, -150)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
seiten = 0
while seiten < 2:
	t.forward(50)
	t.left(90)
	t.forward(100)
	t.left(90)
	seiten += 1
t.end_fill()

# Fenster zeichnen
t.penup()
t.goto(100, -50)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
seiten = 0
while seiten < 4:
	t.forward(30)
	t.left(90)
	seiten += 1
t.end_fill()

t.penup()
t.goto(20, -50)
t.pendown()
t.begin_fill()
seiten = 0
while seiten < 4:
	t.forward(30)
	t.left(90)
	seiten += 1
t.end_fill()

t.done()

