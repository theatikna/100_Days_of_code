from turtle import Turtle
import random

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        random_color = random.choice(["red", "blue", "black", "yellow", "lime"])
        random_start = random.randint(-25, 25) * 10
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random_color)
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(350, random_start)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(5)
    def level_up(self):
        self.car_speed += 5
