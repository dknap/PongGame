from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()
game_is_on = 1
while game_is_on:
    ball.move()
    # bounce the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(ball.heading())

    # detect collision with the paddle
    if ball.distance(player) < 50 and ball.xcor() < -350:
        ball.shot(ball.heading())
        ball.velocity += 1

    # computer's move
    comp.goto(380, ball.ycor())
    if ball.distance(comp) < 50 and ball.xcor() > 360:
        ball.shot(ball.heading())
        ball.velocity += 1

    # ball goes out of bounds
    if ball.xcor() < -380:
        scoreboard.computer_win()
        ball.goto(0, 0)
        ball.velocity = 3
    if ball.xcor() > 380:
        scoreboard.player_win()
        ball.goto(0, 0)
        ball.velocity = 3

    screen.update()

screen.exitonclick()