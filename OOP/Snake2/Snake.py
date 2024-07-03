from turtle import Turtle

class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position) -> None:
        segment = Turtle()
        segment.speed(0)
        segment.pu()
        segment.goto(position)
        segment.color("green")
        segment.shape("square")
        self.segments.append(segment)
        if len(self.segments) == 1:
            segment.color((0.0, 0.9, 0.0))

    def create_snake(self):
        for i in range(3):
            self.add_segment((-i * 20, 0))

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        
        if self.segments:
            self.head.forward(25)

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

    def is_colliding_with_self(self) -> bool:
        for segment in self.segments[1:]:
            if segment.distance(self.head) < 15:
                segment.color("red")
                self.head.color("red")
                return True
        return False
    
    def is_colliding_with_wall(self) -> bool:
        if (self.head.xcor() > 280
        or self.head.xcor() < -280
        or self.head.ycor() > 290
        or self.head.ycor() < -290
        ):
            self.head.color("red")
            self.head.shapesize(2)
            return True
        else:
            return False
        
    def is_colliding_with_food(self, food: Turtle) -> bool:
        if self.head.distance(food) < 23:
            self.head.color("pink")
            return True
        
        self.head.color((0.0, 0.9, 0.0))
        return False
    
    def reset(self) -> None:
        for segment in self.segments:
            segment.ht()
            segment.clear()
        self.segments.clear()
