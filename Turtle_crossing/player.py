# In dieser Datei wird die Klasse Player programmiert.
import turtle
import tkinter as tk

def scale_image(image_path, scale_factor):
    image = tk.PhotoImage(file=image_path)
    width = int(image.width() * scale_factor)
    height = int(image.height() * scale_factor)
    scaled_image = image.subsample(image.width() // width, image.height() // height)
    return scaled_image

screen = turtle.Screen()

STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 14
FINISH_LINE_Y = 280
   
scale_factor = 0.08  # Adjust the scale factor as needed
scaled_car_image = scale_image("Turtle_crossing/car.png", scale_factor)

car_shape = turtle.Shape("image", scaled_car_image)
screen.register_shape(name="car", shape=car_shape)

class Player(turtle.Turtle):
    def __init__(self,color, shape = "car"):
        super().__init__(shape = shape)
        self.color(color)
        self.shapesize(1.5)
        self.penup()
        self.setheading(90)
        self.to_start()
        
        
    def to_start(self):
        self.goto(STARTING_POSITION)

    def switch_side(self):
        self.setx(-self.xcor())
        
    def finish(self):
        return self.ycor() > FINISH_LINE_Y + 5

    def side(self):
        return self.xcor() > 315 or self.xcor() < -315

    def move(self, direction):
        self.setheading(direction)
        self.forward(MOVE_DISTANCE)
        
        



