from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_update()


    def score_update(self):
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_update()

    def game_is_over(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=("Arial",15,"normal"))



