import turtle
import time

#Konstanten
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DELAY = 0.1
SQUARE_SIZE = 20

class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.bgcolor("white")
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

    def check_collision(self):
        if (
            self.snake.head.xcor() > SCREEN_WIDTH // 2 - SQUARE_SIZE
            or self.snake.head.xcor() < -SCREEN_WIDTH // 2
            or self.snake.head.ycor() > SCREEN_HEIGHT // 2 - SQUARE_SIZE
            or self.snake.head.ycor() < -SCREEN_HEIGHT // 2
        ):
            self.reset_game()

        for segment in self.snake.segments[1:]:
            if segment.distance(self.snake.head) < SQUARE_SIZE:
                self.reset_game()
                return

        if self.snake.head.distance(self.food.food) < SQUARE_SIZE:
            self.food_collision()

    def food_collision(self):
        self.food.new_location()
        self.snake.add_segment()
        self.scoreboard.increase_score()

    def reset_game(self):
        for segment in self.snake.segments:
            segment.goto(1000, 1000)
        self.snake.segments.clear()
        self.snake.create_snake()
        self.scoreboard.score = 0
        self.scoreboard.update_scoreboard()

    def run(self):
        frame_rate = 0.1
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
                break
