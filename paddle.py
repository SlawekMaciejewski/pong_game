from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.create_paddle(position_x)

    def create_paddle(self, position_x):
        for index in range(5):
            new_paddle = Turtle(shape="square")
            new_paddle.penup()
            new_paddle.color("white")
            new_paddle.goto(position_x, 0)
            new_paddle.shapesize(stretch_len=1, stretch_wid=5)



