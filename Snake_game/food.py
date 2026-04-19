from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.color("red")
        self.penup()
        self.refresh()

    def refresh(self):

        x_random = random.randint(-280,280)
        y_random = random.randint(-280,280)

        self.goto(x_random,y_random)

