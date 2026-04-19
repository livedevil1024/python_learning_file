from turtle import Turtle, Screen
import random  

screen = Screen()
screen.setup(width=500, height=400)

race_on = False
user_bet = screen.textinput(title="Make your bet",prompt="Enter the turtle which gonna win the race")
Turtle_colour = ["red","blue","green","yellow","orange","purple"]
y_positions = [50,-50,100,-100,150,-150]
turtle_list =[]

for i in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(Turtle_colour[i])
    tim.penup()
    tim.goto(x=-230,y=y_positions[i])
    turtle_list.append(tim)

if user_bet:
    race_on=True

while race_on:

    for t in turtle_list:
        if t.xcor()> 230:
            race_on = False
            winner = t.pencolor( )
            if user_bet == winner:
                print(f"your bet colour turtle {winner} have won the race!")
            else:
                print(f"your bet colour turtle {user_bet} has lost the race")
        random_distance = random.randint(0,10)
        t.forward(random_distance)

screen.exitonclick()