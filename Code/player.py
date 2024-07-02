from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(15)

    def check_finish_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.next_level()
            return True

    def next_level(self):
        self.goto(STARTING_POSITION)
