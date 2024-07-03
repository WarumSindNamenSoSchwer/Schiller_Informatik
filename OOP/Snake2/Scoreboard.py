import turtle

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
        self.scoreboard.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("ds-digital", 24, "normal"))

    def increase_score(self):
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    def reset(self) -> None:
        self.score = 0
        self.update_scoreboard()