#--------------------------------------------------------------------------------------------------------------------

'''
Turtle
'''

'''
Zu erst muss die Library für turtle importiert werden, da man sonst die Funktionen 
der Library nicht benutzen kann.

Das macht man mit dem Schlüsselwort : import
'''

import turtle as t

'''


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def fig():
    t.fillcolor('crimson')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

fig()

t.ht()  
t.done()
'''
t.bgcolor("black")

t.down()
'''
#viereck 1
for c in ('blue', 'red', 'yellow', 'green'):
    t.color(c)
    t.forward(100)
    t.right(90)
'''
t.color("white")
t.circle(100)
t.left(90)
t.forward(200)
t.left(135)
t.forward(143)
t.left(90)
t.forward(143)

#viereck 2
#i = 0
#while i < 3:
  #colors = ['blue', 'red', 'yellow', 'green']
  #t.color(colors[i])
  #i +=1

t.ht()
t.done()