from turtle import Screen, Terminator, Turtle
import Snake
import Game
import Food
import Scoreboard

#Konstanten
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DELAY = 0.1
SQUARE_SIZE = 20

#Bildschirm initialisieren und definieren
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("white")
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.tracer(0)

#spiel Objekte initialisieren
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Tastenfunktion zuweisen
screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")


#Bildwiderholrate setzen
frame_rate = 0.06
last_time = time.time()

while True:
    try:
        current_time = time.time()
        elapsed_time = current_time - last_time

        if elapsed_time >= frame_rate:
            last_time = current_time

            
            snake.move()
            check_collision()   #Collision
            screen.update()

    except Terminator:
        break
