# In dieser Datei wird die Levelanzeige programmiert.
from turtle import Turtle
from time import sleep

FONT = ("Arial", 15, "normal")

    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pos_x = -280
        self.pos_y = 250

        self.highscore = self.load_high_score()
        self.momentan_level = 1

        self.ht()
        self.penup()

        self.goto(self.pos_x, self.pos_y)
        self.write(f"Highscore: {self.highscore}\nLevel {self.momentan_level}", font = FONT)

    def save_high_score(self, level, filename="highscore.txt"):
        with open(filename, 'w') as file:
            file.write(str(level))

    def load_high_score(self, filename="highscore.txt"):
        try:
            with open(filename, 'r') as file:
                level = file.read()
                return int(level)
        except (FileNotFoundError, ValueError):
            return 0 

    def new_level(self):
        self.momentan_level += 1
        self.save_high_score(self.momentan_level)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",align = "center" , font = FONT)
    
    def update(self):
        self.clear()
        self.goto(self.pos_x, self.pos_y)
        self.write(f"Highscore: {self.highscore}\nLevel {self.momentan_level}", font = FONT)

    def reset(self):
        self.clear()
        self.goto(self.pos_x, self.pos_y)
        self.save_high_score(self.momentan_level)
        self.momentan_level = 1
        self.write(f"Highscore: {self.highscore}\nLevel {self.momentan_level}", font = FONT)

