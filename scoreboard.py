from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.player_score = 0
        self.computer_score = 0
        self.write(f"{self.player_score} - {self.computer_score}", False, align=ALIGNMENT, font=FONT)

    def player_win(self):
        self.player_score += 1
        self.update_score()

    def computer_win(self):
        self.computer_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.player_score} - {self.computer_score}", False, align=ALIGNMENT, font=FONT)