from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 3)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.spawn_location()

    def spawn_location(self):
        self.goto(300, random.randrange(-240,240,30))

    def next_level(self):
        self.clear()

    def move(self):
        self.setx(self.xcor() - 10)