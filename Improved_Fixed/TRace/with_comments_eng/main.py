# Import turtle graphics and random modules
from turtle import Screen, Turtle  
import random

# Configure the screen size and background image  
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("TurtleRennen/background/road.gif")

# Configure the turtle attributes - position, color, size
yPosition = [-260, -172, -85, 2, 85, 172, 260]
turtleColors = ["red", "green", "blue", "yellow", "orange", "purple", "teal"]
allTurtle = []

for index in range(7):
    t = Turtle(shape="turtle") # Create a new turtle 
    t.speed(0) # Set turtle speed to fastest
    t.shapesize(3) # Make turtle size bigger
    t.penup() # Lift up pen so no lines are drawn
    t.goto(x=-360, y= yPosition[index]) # Position turtle horizontally and vertically
    t.color(turtleColors[index]) # Set turtle color
    allTurtle.append(t) # Add new turtle to list

isOn = True # Variable to control main loop
ALIGN = "right" 
FONT = ('Arial', 15 , 'normal') 

userBet = screen.textinput(title="Enter your bet", prompt="Enter your bet, which turtle color? : ") # Get user's bet

while isOn:
    for t in allTurtle:
        if t.xcor() > 330: # Check if turtle passed finish line
            isOn = False # Stop race
            winner = t.pencolor() # Get winning turtle's color
            t.pencolor('white') # Set text color to white
            if winner == userBet: # Check if user guessed winner
                t.write(f"You guessed the winner {winner} correct", font=FONT, align=ALIGN)
            else:
                t.write(f"You didn't guess the winner {winner} correct", font=FONT, align=ALIGN)
        randomPace = random.randint(0, 15) # Get random speed 
        t.forward(randomPace) # Move turtle forward

screen.exitonclick() # Wait for click to exit
