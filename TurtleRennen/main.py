from turtle import Screen, Turtle
import random
from PIL import Image

#configuring the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("TurtleRennen/background/road.gif")

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
                im1 = Image.open("TurtleRennen/background/Bitches.jpg")
                im1.show()
            else:
                t.write(f"You didn't guess the winner {winner} correct", font=FONT, align=ALIGN)
                im2 = Image.open("TurtleRennen/background/JC.png")
                im2.show()
        randomPace = random.randint(0, 20)
        t.forward(randomPace)



screen.exitonclick()