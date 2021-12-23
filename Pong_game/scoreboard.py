from turtle import Turtle
WINNING_POINT = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.winning_point = WINNING_POINT
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l = 0
        self.r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r, align="center", font=("Courier", 80, "normal"))



    def l_score(self):
        self.l += 1
        self.update_scoreboard()


    def r_score(self):
        self.r += 1
        self.update_scoreboard()

    def print_winner(self):
        winner = "left"
        if self.r == self.winning_point:
            winner = "right"
        self.goto(0,0)
        self.write(f"The {winner} hand player has won!", align="center", font=("Courier", 35, "normal"))





