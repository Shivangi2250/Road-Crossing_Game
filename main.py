import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("light green")
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars=CarManager()
scoreboard=Scoreboard()

screen.onkeypress(player.move_up,"w")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # scoreboard.level1()
    screen.update()
    cars.create_car()
    cars.move_car()
    for car in cars.all_cars:
        if player.distance(car)<30:
            scoreboard.you_lose()
            game_is_on=False

        elif player.ycor()==290:
            scoreboard.level_2()
            cars.speed_car()
            player.start_again()
            # if player.ycor() == 290:    #not working
            #     scoreboard.you_won()
            #     game_is_on=False

















screen.exitonclick()