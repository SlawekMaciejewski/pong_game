from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x):
        """
        Paddle class. It's creating paddle for player in the pass x position.
        :self.create_paddle(position_x): list of the snake segments
        """
        super().__init__()
        self.create_paddle(position_x)

    def create_paddle(self, position_x):
        """
        It's creating paddle for player in the pass x position. Position y is 0..
        :return: None
        """
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position_x, 0)

    def go_up(self):
        """
        Function move up a paddle.
        :return: None
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Function move down a paddle.
        :return: None
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



