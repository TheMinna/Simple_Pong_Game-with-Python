from turtle import Turtle

FONT = ("Courier", 24, "normal")

ALIGMENT_LEFT = 'left'
# ALIGMENT_RIGHT = 'right'


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align='center', font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", move=False, align='left',
                   font=FONT)  # maybe put aligment as a parameter?

    def update_scoreboard(self):
        self.write(f"{self.score}", move=False, align='left',
                   font=FONT)  # maybe put aligment as a parameter?
