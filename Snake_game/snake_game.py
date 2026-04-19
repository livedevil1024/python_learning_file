from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake()
screen.onkey(snake.Up,"w")
screen.onkey(snake.Down,"s")
screen.onkey(snake.Left,"a")
screen.onkey(snake.Right,"d")

food = Food()
score =Scoreboard()
game_over = True

while game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_increase()
        snake.extend_segments()

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()