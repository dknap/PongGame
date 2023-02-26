from turtle import Turtle

UP = 90
DOWN = -90


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-370, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)