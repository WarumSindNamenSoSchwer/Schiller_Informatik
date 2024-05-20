# In dieser Datei werden Objekte instanziiert und das Spiel wird ausgeführt.

from time import sleep
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
screen.onkeypress(lambda: player.bewegen(90), "w")
screen.onkeypress(lambda: player.bewegen(180), "a")
screen.onkeypress(lambda: player.bewegen(-90), "s")
screen.onkeypress(lambda: player.bewegen(360), "d")

# Instanziieren des Auto-Managers (d.h. der Klasse, die Autos erstellt und bewegt)
car_manager = CarManager()

# Beginn der Spielschleife
game_is_on = True
while game_is_on:
    # Jede Hundertstelsekunde passiert Folgendes:
    sleep(0.001)
    screen.update()
    scoreboard.update()

    car_manager.move_cars()
    
    if player.seite():
        player.andere_seite()

    if player.ziel():
        player.zum_anfang()
        scoreboard.neues_level()






screen.exitonclick()

    
