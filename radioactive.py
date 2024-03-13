import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle
t = turtle.Turtle()
t.speed(0)
#t.ht()

def first_circle():
    t.penup()
    t.goto(0,-100)
    t.fillcolor('yellow')
    t.pensize(10)
    t.begin_fill()
    t.pendown()
    t.circle(200)
    t.end_fill()
    t.penup()

def second_circle():
    t.goto(0,-20)
    t.pensize(0)
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.pendown()
    t.circle(120)
    t.end_fill()
    t.penup()

def third_circle():
    t.goto(0,60)
    t.fillcolor('black')
    t.begin_fill()
    t.pendown()
    t.circle(40)
    t.end_fill()
    t.penup()

def lines():
    t.pencolor('blue')
    t.goto(0,100)
    t.pendown()
    t.setheading(70)
    t.forward(130)
    t.left(60)
    t.circle(60,100)
    t.setheading(100)



def main():
    first_circle()
    second_circle()
    third_circle()
    lines()
    screen.exitonclick()



if __name__ == "__main__":
    main()