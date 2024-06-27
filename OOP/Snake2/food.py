import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.new_location()

    def new_location(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
