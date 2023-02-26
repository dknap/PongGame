from turtle import Screen
from paddle import Paddle
from ball import Ball

# screen setting
screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# create paddles
player = Paddle()
player.set_position(0)

comp = Paddle()
comp.set_position(1)

# movement
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

# game-flow
ball = Ball()
game_is_on = 1
while game_is_on:
    ball.move()
    screen.update()

    # ball bouncing
    if ball.distance(x=ball.xcor(), y=300) < 15 or ball.distance(x=ball.xcor(), y=-300) < 15:
        ball.bounce(ball.heading())

    # detect collision with paddle
    if ball.distance(x=-360, y=player.ycor()) < 15:
        ball.shot(ball.heading())


screen.exitonclick()