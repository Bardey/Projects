from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Data.txt") as file:
            self.high_score= int(file.read())
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.display_score()


    def plus_point(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.high_score = self.read_score_file()
        self.display_score()

    def read_score_file(self):
        with open("Data.txt", mode="r") as file:
            score = int(file.read())
        return score

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.hideturtle()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
