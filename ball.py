from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("slowest")
        self.setheading(random.randint(140, 220))
        print(self.heading())

    def move(self):
        self.forward(3)
