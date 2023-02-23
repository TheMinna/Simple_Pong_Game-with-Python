from turtle import Turtle

MOVE_DISTANCE = 10
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, start_tuple):
        super().__init__()
        self.create_paddle(start_tuple)

    def create_paddle(self, start_tuple):
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(start_tuple)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        # self.setheading(UP)
        # self.forward(MOVE_DISTANCE)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
