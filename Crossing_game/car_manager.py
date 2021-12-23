from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(self.random_color())
        self.setheading(180)
        self.goto_random_pos()

    def goto_random_pos(self):
        rpos_y = random.randrange(-240,240, 25)
        self.goto(300,rpos_y)
    def random_color(self):
        return random.choice(COLORS)

    def move(self):
        self.forward(5)






