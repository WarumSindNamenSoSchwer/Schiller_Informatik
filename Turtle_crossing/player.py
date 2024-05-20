# In dieser Datei wird die Klasse Player programmiert.
from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self,color, shape = "square"):
        super().__init__(shape = shape)
        self.color(color)
        self.shapesize(1.5)
        self.penup()
        self.setheading(90)
        self.zum_anfang()
        
    def zum_anfang(self):
        self.goto(STARTING_POSITION)

    def andere_seite(self):
        self.setx(-self.xcor())
        
    def ziel(self):
        return self.ycor() > FINISH_LINE_Y + 5

    def seite(self):
        return self.xcor() > 315 or self.xcor() < -315

    def bewegen(self, direction):
        self.setheading(direction)
        self.forward(MOVE_DISTANCE)
        
        


