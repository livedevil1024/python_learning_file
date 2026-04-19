from turtle import Turtle, Screen
import turtle
import random

jimmy = Turtle()
jimmy.shape("turtle")
turtle.colormode(255)

def shape(x) :
    angle = 360 / x
    
    for _ in range(x):
        jimmy.fd(80)
        jimmy.right(angle)

def random_colour():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_colours = (r,b,g)
    return random_colours

jimmy.speed("fastest")

def Draw_sprograph(size_of_gap):

    for _ in range(int(360 /size_of_gap)):
        jimmy.color(random_colour()) 
        jimmy.circle(100)
        jimmy.setheading(jimmy.heading() + size_of_gap)
    
Draw_sprograph(1)


Screen = turtle.Screen()
Screen.exitonclick()
