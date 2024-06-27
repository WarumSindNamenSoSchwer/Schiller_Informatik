import turtle
import random

#Konstanten
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DELAY = 0.1
SQUARE_SIZE = 20

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.new_location()

    def new_location(self):
        x = random.randint(-SCREEN_WIDTH // 2 + SQUARE_SIZE, SCREEN_WIDTH // 2 - SQUARE_SIZE)
        y = random.randint(-SCREEN_HEIGHT // 2 + SQUARE_SIZE, SCREEN_HEIGHT // 2 - SQUARE_SIZE)
        self.food.goto(x, y)
