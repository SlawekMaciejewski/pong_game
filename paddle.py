from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.segments = []
        self.create_paddle(position_x)

    def create_paddle(self, position_x):
        y = 0
        for index in range(5):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position_x, y)
            self.segments.append(new_segment)
            y -= 20


