from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle, MOVE_DISTANCE
from scoreboard import Scoreboard
# from walls import WallsEnd, WallsBounce
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)  # NEEDS TO HAVE TO REFRESH SET TO AFTER MOVING

scoreboard_l = Scoreboard((-200, 260))
scoreboard_r = Scoreboard((200, 260))

ball = Ball()

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

# #GAME OVER walls:
# wall_end_left = WallsEnd((-400, 0))
# wall_end_right = WallsEnd((400, 0))

# # BOUNCE walls:
# wall_bounce_up = WallsBounce((0, 300))
# wall_bounce_down = WallsBounce((0, -300))


screen.listen()
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

speed_index = 0

game_on = True
while game_on:
    screen.update()
    # Must adjust ball speed and screen update/sleep
    time.sleep(ball.move_speed)
    ball.move()

    if paddle_left.ycor() > 280:
        paddle_left.setposition(-350, paddle_left.ycor() - MOVE_DISTANCE)

    if paddle_left.ycor() < -280:
        paddle_left.setposition(-350, paddle_left.ycor() + MOVE_DISTANCE)

    if paddle_right.ycor() > 280:
        paddle_right.setposition(350, paddle_right.ycor() - MOVE_DISTANCE)

    if paddle_right.ycor() < -280:
        paddle_right.setposition(350, paddle_right.ycor() + MOVE_DISTANCE)

    if ball.distance(paddle_left) < 50 and ball.xcor() == -340:
        ball.bounce_paddle()
        ball.move_speed *= 0.8

        # MUST FIX THE DOUBLE BOUNCE!

    if ball.distance(paddle_right) < 50 and ball.xcor() == 340:
        ball.bounce_paddle()
        ball.move_speed *= 0.8

        # MUST FIX THE DOUBLE BOUNCE!

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_wall()

    if ball.xcor() > 400:
        scoreboard_l.increase_score()
        ball.goto(0, 0)
        ball.move()
        ball.move_speed = 0.1

    if ball.xcor() < -400:
        scoreboard_r.increase_score()
        ball.goto(0, 0)
        ball.move()
        ball.move_speed = 0.1

screen.exitonclick()
