from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(F"Level: {self.level} ", font=FONT)

    def game_over(self):
        self.goto(0, -280)
        self.write("GAME OVER", align="CENTER", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

