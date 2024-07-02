from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


def game():
    #Screen setup
    screen = Screen()
    screen.setup(600, 600)
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    #Key bindings
    screen.listen()
    screen.onkeypress(snake.up, "w")
    screen.onkeypress(snake.down, "s")
    screen.onkeypress(snake.left, "a")
    screen.onkeypress(snake.right, "d")

    #Frame rate
    frame_rate = 0.06
    last_time = time.time()

    game_is_on: bool = True

    while game_is_on:
        current_time = time.time()
        elapsed_time = current_time - last_time

        if elapsed_time >= frame_rate:
            last_time = current_time
            
            screen.update()
            snake.move()
            scoreboard.update_scoreboard()

            #Food collision
            if snake.is_colliding_with_food(food):
                snake.add_segment(snake.segments[-1].position())
                food.new_location()
                scoreboard.increase_score()

            #Game ending collision
            if snake.is_colliding_with_self() or snake.is_colliding_with_wall():
               game_is_on = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake Game")

game()
screen.update()
player_wants_to_play = True
while player_wants_to_play == True:
    player_input = screen.textinput("Wannt to play again?", "Wannt to play again? (y/n)")
    if player_input == "n":
        player_wants_to_play = False
        screen.bye()

    elif player_input !="y":
        continue
    
    else:        
        screen.clearscreen()
        game()
        screen.update()
