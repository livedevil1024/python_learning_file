from turtle import Turtle

from nbformat import read

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_update()


    def score_update(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",20,"normal"))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_update()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.score_update()

    

