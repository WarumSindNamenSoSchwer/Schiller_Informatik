from turtle import Screen, Turtle
import random

#configuring the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("TurtleRennen/background/road.gif")

#configuring the turtles
yPosition = [-260, -172, -85, 2, 85, 172, 260]
turtleColors = ["red", "green", "blue", "yellow", "orange", "purple", "teal"]
allTurtle = []

for index in range(7):
    t = Turtle(shape="turtle")
    t.speed(0)
    t.shapesize(2)
    t.penup()
    t.goto(x=-360, y= yPosition[index])
    t.color(turtleColors[index])
    t.pendown()
    allTurtle.append(t)

isOn = True
ALIGN = "right"
FONT = ("Courier", 16, "bold")

userBet = screen.textinput(title="Enter your bet", prompt="Enter your bet, which turtle color? : ")

while isOn:
    for t in allTurtle:
        if t.xcor() > 330:
            isOn = False
            winner = t.pencolor()
            if winner == userBet:
                t.write(f"You guessed the winner {winner} correct", font=FONT, align=ALIGN)
            else:
                t.write(f"You didn't guess the winner {winner} correct", font=FONT, align=ALIGN)
        randomPace = random.randint(0, 15)
        t.forward(randomPace)

screen.exitonclick()