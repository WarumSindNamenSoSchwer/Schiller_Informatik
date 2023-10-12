import turtle as t

t.fillcolor("red")
t.begin_fill()
seiten = 0
while seiten < 4:
	t.forward(150)
	print(t.position())
	t.left(90)
	seiten += 1
t.end_fill()

#Dach zeichnen
t.penup()
t.goto(150, 150)
t.pendown()
t.fillcolor("green")
t.begin_fill()
t.left(90)
t.left(60)
t.forward(87)
t.left(60)
t.forward(87)
t.left(150)
t.forward(150)
t.end_fill()

# Tür zeichnen
t.penup()
t.goto(55, 0)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
seiten = 0
while seiten < 2:
	t.forward(40)
	t.left(90)
	t.forward(80)
	t.left(90)
	seiten += 1
t.end_fill()

# Fenster zeichnen
t.penup()
t.goto(100, 70)
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
t.goto(20, 70)
t.pendown()
t.begin_fill()
seiten = 0
while seiten < 4:
	t.forward(30)
	t.left(90)
	seiten += 1
t.end_fill()

t.ht()

t.done()

