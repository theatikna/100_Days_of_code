from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.write(f"LEVEL : {self.level}", "center", font=("Courier",30,"normal"))

    def increse_level(self):
        self.level += 1
        self.clear()
        self.goto(-200,250)
        self.write(f"LEVEL : {self.level}", "center", font=("Courier",30,"normal"))
    def game_over(self):      
        self.goto(-100,0)

        self.write(f"GameOver", "center", font=("Courier",30,"normal"))
