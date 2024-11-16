import turtle
import random
import time

# Game Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DELAY = 0.1
SQUARE_SIZE = 20

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

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.scoreboard = turtle.Turtle()
        self.scoreboard.speed(0)
        self.scoreboard.shape("square")
        self.scoreboard.color("black")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(0, SCREEN_HEIGHT // 2 - 60)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("ds-digital", 24, "normal"))

    def increase_score(self):
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.bgcolor("green")
        self.window.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.window.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.window.listen()
        self.window.onkeypress(self.snake.up, "w")
        self.window.onkeypress(self.snake.down, "s")
        self.window.onkeypress(self.snake.left, "a")
        self.window.onkeypress(self.snake.right, "d")
        self.window.onkeypress(self.reset_game, "r")

    def check_collision(self):
        # Check collision with borders
        if (
            self.snake.head.xcor() > SCREEN_WIDTH // 2 - SQUARE_SIZE
            or self.snake.head.xcor() < -SCREEN_WIDTH // 2
            or self.snake.head.ycor() > SCREEN_HEIGHT // 2 - SQUARE_SIZE
            or self.snake.head.ycor() < -SCREEN_HEIGHT // 2
        ):
            self.reset_game()

        # Check collision with snake body
        for segment in self.snake.segments[1:]:
            if segment.distance(self.snake.head) < SQUARE_SIZE - 10:
                self.reset_game()
                return

        # Check collision with food
        if self.snake.head.distance(self.food.food) < SQUARE_SIZE:
            self.food_collision()

    def food_collision(self):
        self.food.new_location()
        self.snake.add_segment()
        self.scoreboard.increase_score()

    def reset_game(self):
        for segment in self.snake.segments:
            segment.goto(1000, 1000)  # Move segments off-screen
        self.snake.segments.clear()
        self.snake.create_snake()
        self.scoreboard.score = 0
        self.scoreboard.update_scoreboard()

    def run(self):
        frame_rate = 0.06
        last_time = time.time()

        while True:
            try:
                current_time = time.time()
                elapsed_time = current_time - last_time

                if elapsed_time >= frame_rate:
                    last_time = current_time
                    self.snake.move()
                    self.check_collision()
                    self.window.update()

            except turtle.Terminator:
                self.reset_game()


if __name__ == "__main__":
    game = Game()
    game.run()
