from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed=-STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance=random.randint(1,6)  #we create a random chance means if random_chance is equal to 1 then only new car is created and
        # this will happen after it reaches the 6 and every new car gets equal time of 6
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            theColor = random.choice(COLORS)
            new_car.color(theColor)
            new_car.penup()
            new_car.shapesize(stretch_wid=1.5, stretch_len=2.5)
            random_y=random.randint(-250,250)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_car(self):
        self.car_speed-= MOVE_INCREMENT






