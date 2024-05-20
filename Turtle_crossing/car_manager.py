# In dieser Datei wird der Auto-Manager programmiert, der Autos erstellt
# und bewegt.
import player
from random import randint
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2

class CarManager:
    def __init__(self):
        self.speed = MOVE_INCREMENT
        self.car_list = []
        
    def spawn_cars(self):
        for i in range(6):
            car = player.Player(color = COLORS[i])
            car.goto(280, randint(-230, 280))
            car.setheading(180)
            self.car_list.append(car)    

    def move_cars(self):
        for car in self.car_list:
            car.forward(randint(0, 3))
            

