from turtle import Turtle
import numpy
FONT = ("Courier", 24, "normal")
PROBABILITY_CHANGE = 0.025


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.refresh()
        self.sleep_time = 0.1
        self.probability_change = 0


    def refresh(self):
        self.clear()
        self.goto(-270, 250)
        self.write(f"Level : {self.level}", font=FONT)

    def lvlup(self):
        self.level += 1
        self.refresh()
        self.sleep_time *= 0.7
        self.probability_change += PROBABILITY_CHANGE

    def gameover(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def probability(self):
        return numpy.random.choice(numpy.arange(0, 2), p=[0.9 - self.probability_change, 0.1 + self.probability_change])




