from turtle import Turtle

MOVE_DISTANCE = 20
START_PAD_LENGTH = 5


class Paddle(Turtle):
    def __init__(self, start_pad_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=START_PAD_LENGTH)  # standard size is 20 pixels
        self.goto(start_pad_pos)

    def go_right(self):
        if self.xcor() < 340:
            self.setheading(0)
            self.forward(MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() > -340:
            self.setheading(180)
            self.forward(MOVE_DISTANCE)

    def shrink(self):
        self.shapesize(stretch_len=START_PAD_LENGTH/2)
