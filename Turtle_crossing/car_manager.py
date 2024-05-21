# In dieser Datei wird der Auto-Manager programmiert, der Autos erstellt
# und bewegt.
import player
import random as r
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 2

class CarManager:
    def __init__(self):
        self.car_list = []
        
    def spawn_cars(self):
        if r.randint(1,132) == 1:
            car = player.Player(r.choice(COLORS))
            car.goto(280, r.randint(-230, 250))
            car.setheading(180)
            self.car_list.append(car)    

    def move_cars(self):
        for car in self.car_list:
            car.forward(r.randint(0, 2))

            if car.xcor() < -320:
                car.clear()
                car.ht()
                self.car_list.remove(car)
            

