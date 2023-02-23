from turtle import Turtle


class WallsEnd(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('pink')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=30, stretch_len=0.5)
        self.speed('normal')
        self.setposition(position)


class WallsBounce(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('pink')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=40)
        self.speed('normal')
        self.setposition(position)
