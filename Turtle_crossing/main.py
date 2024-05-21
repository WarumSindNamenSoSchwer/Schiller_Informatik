# In dieser Datei werden Objekte instanziiert und das Spiel wird ausgeführt.

from time import sleep, time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Instanziieren des Screens und Setup auf 600x600 Pixel
screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

# Instanziieren des Scoreboards
scoreboard = Scoreboard()

# Instanziieren des Spielers (d.h. der Schildkrötenfigur)
player = Player("green", "turtle")


# Tastatur-Steuerung auf dem Screen einstellen
screen.listen()
screen.onkeypress(lambda: player.move(90), "w")
screen.onkeypress(lambda: player.move(180), "a")
screen.onkeypress(lambda: player.move(-90), "s")
screen.onkeypress(lambda: player.move(360), "d")

# Instanziieren des Auto-Managers (d.h. der Klasse, die Autos erstellt und bewegt)
car_manager = CarManager()

# 50 updates per second
FRAME_RATE = 0.03
last_time = time()

# Beginn der Spielschleife
game_is_on = True
while game_is_on:
    current_time = time()
    elapsed_time = current_time - last_time

    if elapsed_time >= FRAME_RATE:
        last_time = current_time
        
    screen.update()
    scoreboard.update()

    car_manager.spawn_cars()
    car_manager.move_cars()
    
    if player.side():
        player.switch_side()

    if player.finish():
        player.to_start()
        scoreboard.new_level()






screen.exitonclick()

    
