# In dieser Datei wird die Klasse Player programmiert.
from turtle import Turtle

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, shape, color):
        super().__init__(shape = shape)
        self.color(color)
        self.penup()
        self.setheading(90)
        
        
        
        


    def bewegen(self, direction):
        self.setheading(direction)
        self.forward(MOVE_DISTANCE)
        
        



