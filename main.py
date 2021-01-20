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
time.sleep(0.1)

screen.update()
screen.exitonclick()
