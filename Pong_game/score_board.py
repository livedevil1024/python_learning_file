from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.updated_score()

    def updated_score(self):
        self.write(f"Score {self.score}", align="center",font=("Courier",20,"normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.updated_score()