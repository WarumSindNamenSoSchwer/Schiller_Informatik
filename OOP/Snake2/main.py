from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

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

GameIsOn: bool = True

while GameIsOn:
    current_time = time.time()
    elapsed_time = current_time - last_time

    if elapsed_time >= frame_rate:
        last_time = current_time
        
        screen.update()
        snake.move()
        scoreboard.update_scoreboard()

        if snake.is_colliding_with_food(food):
            snake.add_segment()
            food.new_location()
            scoreboard.increase_score()

        #Game ending collision
        if snake.is_colliding_with_self() or snake.is_colliding_with_wall():
           GameIsOn = False
           """  response: str = screen.textinput("Replay?", "Would you like to play again?")
            
            

            if response == "yes":
                print(1)
                snake.reset()
                scoreboard.reset()
                food.new_location()
                snake.create_snake()
                snake.move()
                screen.update()
                screen.listen()
                GameIsOn = True
            else:
                print(2)
                GameIsOn = False """

screen.update()
screen.mainloop()
