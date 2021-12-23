import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

# colors = colorgram.extract("image.jpg", 30)
# color_list = []
#
# for i in range(len(colors)):
#     rgb = colors[i].rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     color_list.append((r,g,b))

teddy = Turtle()


color_list = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]
teddy.hideturtle()
teddy.speed(0)
y = -250
x = -250
teddy.penup()
teddy.setposition(x,y)
for i in range(10):
    x = -250
    teddy.sety(y)
    for j in range(10):
        teddy.setx(x)
        teddy.dot(20, random.choice(color_list))
        x += 50
    y += 50








screen = Screen()
screen.exitonclick()


