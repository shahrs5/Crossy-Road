from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.display_level()
        self.speed = 0.1

    def display_level(self):
        self.clear()
        self.write(f"Level : {self.level}", False, align="center", font=FONT)

    def next_level(self):
        self.speed *= 0.9
        self.level += 1
        self.display_level()


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Gameover! Your Score is {self.level}", False, align="center", font=FONT)
