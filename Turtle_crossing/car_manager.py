# In dieser Datei wird der Auto-Manager programmiert, der Autos erstellt
# und bewegt.
import player
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2

class CarManager:
    def __init__(self):
        self.speed = MOVE_INCREMENT
        self.car_list = []
        for i in range(10):
            car = player.Player(color = COLORS[randint(0,5)])
            self.car_list.append(car)
        
        
    def move_cars(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)
