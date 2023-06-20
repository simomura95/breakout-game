from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self, start_ball):
        super().__init__()
        # self.speed("fastest")
        self.start_pos = start_ball
        self.speed = 8
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(start_ball)
        self.setheading(random.choice([45, 135]))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # standard size is 20 pixels

    def move(self):
        self.forward(self.speed)

    def bounce_rl(self):
        self.setheading(180-self.heading())

    def bounce_ud(self):
        self.setheading(360-self.heading())
