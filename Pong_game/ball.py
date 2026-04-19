from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_change = 10
        self.y_change = 10
        self.move()
        self.bounce_speed = 0.1

    def move(self):
        x_new = self.xcor() + self.x_change
        y_new = self.ycor() + self.y_change
        self.goto(x_new,y_new)
    
    def bounce_y(self):
        self.y_change *= -1

    def bounce_x(self):
        self.x_change *= -1
        self.bounce_speed *= 0.9

    def ball_reset(self):
        self.bounce_speed = 0.1
        self.goto(0,0)
        self.bounce_x()
        
