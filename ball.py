from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.setheading(randint(180, 260))
        print(self.heading())

    def bounce(self, angle):
        self.setheading(-angle)

    def shot(self, angle):
        self.setheading(180 - angle)

    def move(self):
        self.forward(3)