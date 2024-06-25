import turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    
    def create_snake(self):
        for _ in range(3):
            self.add_segment()

    def add_segment(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.penup()
        segment.color("black")
        segment.shape("square")
        self.segments.append(segment)
    
    def move(self):
        for index in range(len(self.segments) -1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
            
        if self.segments:
            self.head.forward(SQUARE_SIZE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0) 
