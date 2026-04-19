from turtle import Turtle


SNAKE_POSITION = [(0,0) ,(-20,0) ,(-40,0) ]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT =180
RIGHT =0
class Snake:

    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]
        

    def create_snake(self):
        for pos in SNAKE_POSITION:
            self.add_segment(pos)
            

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend_segments(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x_head = self.segments[i-1].xcor()
            y_head = self.segments[i-1].ycor()
            self.segments[i].goto(x_head,y_head)   
        self.head.forward(MOVE_DISTANCE)
    
    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
