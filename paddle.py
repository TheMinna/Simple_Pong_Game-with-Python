from turtle import Turtle

STARTING_POSITION_Y = [20, 0, -20]
STARTING_POSITION_X = [380, -380]

class Paddle():
    def __init__(self, x_cor):
        self.segments = []
        self.create_paddle(STARTING_POSITION_Y)
        
    def create_paddle(self, x_cor):
        for position in STARTING_POSITION_Y:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.speed('normal')
            new_segment.setposition(-370, position) #X_cor must be negative in the right side
