import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Shaheer's Crossy Road")

game_is_on = True
player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move,"Up")

while game_is_on:

    time.sleep(scoreboard.speed)
    screen.update()

    if random.randint(0,5) == 1:
        newcar = CarManager()
        cars.append(newcar)

    for i in cars:
        i.move()
        x = player.xcor()
        if (player.xcor() + 30) >= i.xcor() >= (player.xcor() - 30) and (player.ycor() + 10) >= i.ycor() >= (player.ycor() - 10):
            game_is_on = False
            scoreboard.game_over()

    if player.check_finish_level():
        scoreboard.next_level()
        for i in cars:
            i.hideturtle()
        cars = []


screen.exitonclick()

