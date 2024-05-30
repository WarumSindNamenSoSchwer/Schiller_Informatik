# In dieser Datei wird der Auto-Manager programmiert, der Autos erstellt
# und bewegt.
import player
import random as r
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_increment = 0
        self.max_spawn_amount = 8

    def spawn_cars(self):
        if r.randint(1,140) == 1 and self.car_list.__len__() < self.max_spawn_amount:
            car = player.Player(r.choice(COLORS))
            car.goto(280, r.randint(-220, 250))
            car.setheading(180)
            self.car_list.append(car)    

    def move_cars(self):
        for car in self.car_list:
            if r.randint(0, 10) == 1:   
                car.forward(STARTING_MOVE_DISTANCE + self.move_increment)

            if car.xcor() < -320:
                car.clear()
                car.ht()
                self.car_list.remove(car)
            

    def level_up(self):
        self.move_increment += 1
        self.max_spawn_amount += 10

    def reset_values(self):
        self.move_increment = 0
        self.max_spawn_amount = 8

    def clear_cars(self):
        for car in self.car_list[:]:  # Create a copy of the list for iteration
            car.clear()
            car.hideturtle()
        self.car_list.clear()
