import time
import random
import numpy
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()

screen.onkey(player.up, "Up")
scoreboard = Scoreboard()


cars = []


game_is_on = True
while game_is_on:
    # Player reaches finish line
    if player.ycor() > player.finish_y:
        player.reset_pos()
        scoreboard.lvlup()
    # Cars randomly generated
    if scoreboard.probability():
        car = CarManager()
        cars.append(car)
    for i in cars:
        # Collision with cars
        if player.distance(i) < 30:
            game_is_on = False
            scoreboard.gameover()
            break
        if i.xcor() < -300:
            i.hideturtle()
            cars.remove(i)
        i.move()

    time.sleep(scoreboard.sleep_time)
    screen.update()

screen.exitonclick()
