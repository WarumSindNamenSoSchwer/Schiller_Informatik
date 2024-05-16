# In dieser Datei werden Objekte instanziiert und das Spiel wird ausgeführt.

from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Instanziieren des Screens und Setup auf 600x600 Pixel
screen = Screen()
screen.setup(600, 600)

# Instanziieren des Scoreboards
scoreboard = Scoreboard()

# Instanziieren des Spielers (d.h. der Schildkrötenfigur)
player = Player("turtle", "green")


# Tastatur-Steuerung auf dem Screen einstellen
screen.listen()
screen.onkeypress(lambda: player.bewegen(180), "w")

# Instanziieren des Auto-Managers (d.h. der Klasse, die Autos erstellt und bewegt)

# Beginn der Spielschleife
game_is_on = True
while game_is_on:
    # Jede Hundertstelsekunde passiert Folgendes:
    sleep(0.01)
    screen.update()







screen.exitonclick()

    
