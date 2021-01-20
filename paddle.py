from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.create_paddle(position_x)

    def create_paddle(self, position_x):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position_x, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



