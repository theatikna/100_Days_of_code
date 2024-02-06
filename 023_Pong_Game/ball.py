from turtle import Turtle
import random as r


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.y_move = r.randint(1, 10)
        self.x_move = r.randint(1, 10)
        self.ball_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.ball_speed = 0.1
