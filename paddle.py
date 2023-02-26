from turtle import Turtle

positions = [(-370, 0), (360, 0)]

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.position()[1] < 260:
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.position()[1] > -240:
            self.goto(self.xcor(), self.ycor() - 20)

    def set_position(self, pos):
        self.goto(positions[pos])