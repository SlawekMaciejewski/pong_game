from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("THE PONG GAME")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle(position_x=350)
l_paddle = Paddle(position_x=-350)

scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    # Detect when the R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_l_score()
    # Detect when the L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()
