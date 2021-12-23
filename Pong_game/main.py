import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.winning_point = int(turtle.textinput("Starting the game...", "How much point?"))


screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
game_is_on = True
while game_is_on:
    ball.move()
    screen.update()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    # Collision with right paddle
    if (ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50) and abs(ball.xcor()) > 325:
        ball.bounce_x()

    # Missing the ball
    if ball.xcor() > 370:
        scoreboard.l_score()
        ball.reset_position()
        ball.random_redirect()

    if ball.xcor() < -370:
        scoreboard.r_score()
        ball.reset_position()
        ball.random_redirect()

    if scoreboard.l == scoreboard.winning_point or scoreboard.r == scoreboard.winning_point:
        game_is_on = False
        scoreboard.print_winner()



    time.sleep(ball.speed)






screen.exitonclick()
