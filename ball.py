from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        # self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        # self.speed('slowest')
        self.color('white')
        self.setposition(0, 0)
        # self.ball_heading()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # def ball_heading(self):
    #     random_angle = random.randint(1, 360)
    #     while self.heading() % 90 == 0:
    #         self.setheading(random_angle)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_paddle(self):
        self.x_move *= -1

    def bounce_wall(self):
        self.y_move *= -1
