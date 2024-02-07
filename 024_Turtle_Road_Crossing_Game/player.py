from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.goto(0,-280)
        self.setheading(90)
    def up_move(self):
        self.forward(10)
    def right_move(self):
        x = self.xcor() + 10
        self.goto(x, self.ycor())
    def left_move(self):
        x = self.xcor() - 10
        self.goto(x,self.ycor())

    def go_to_start(self):
        self.goto(0,-280)
    def is_at_finish(self):
        if self.ycor() >=280:
            return True
        else :
            return False

