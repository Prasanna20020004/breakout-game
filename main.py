from turtle import Screen
from bricks import Bricks
from ball import Ball
from paddle import Paddle
from scoreboard import Score
import time

screen = Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)

brick = Bricks(30)
paddle = Paddle()
ball = Ball()
score = Score()

screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")

game_on = True
total_bricks = len(brick.bricks)
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.ycor() < -290:
        game_on = False

    if ball.distance(paddle) < 25:
        ball.bounce_y()

    for a_brick in brick.bricks:
        if ball.distance(a_brick) < 30:
            ball.bounce_y()
            brick.remove(a_brick)
            score.update_score()
            score.display()
            total_bricks -= 1

    if total_bricks == 0:
        score.display_end_score()
        game_on = False

screen.exitonclick()
