from turtle import Screen
from paddle import Paddle

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

game_is_on = 1
while game_is_on:
    screen.update()

screen.exitonclick()