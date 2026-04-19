from turtle import Turtle, Screen

tim = Turtle()

def forward1():
    tim.forward(10)

def backward1():
    tim.backward(10)

def anticlockwise():
    tim.left(22.5)

def clockwise():
    tim.right(22.5)
def Clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.onkey(key="w", fun=forward1)
screen.onkey(key="s", fun=backward1)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c",fun=Clear)
screen.listen()

screen.exitonclick()
