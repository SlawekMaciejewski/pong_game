from turtle import Screen, Turtle
from paddle import Paddle
import time

screen = Screen()
screen.title("THE PONG GAME")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)

screen.listen()
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # The screen delay is displayed after 0.1s and then refresh the screen.

screen.exitonclick()
