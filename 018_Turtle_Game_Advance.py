import random
import turtle
import colorgram
from turtle import Screen, Turtle
def square(jim):
    for i in range(4):
        jim.forward(100)
        jim.right(90)

def dash(jim):
    for _ in range(10):
        jim.forward(10)
        jim.penup()
        jim.forward(10)
        jim.pendown()
        jim.forward(10)
def shapes(jim):
    jim.speed("fastest")
    for i in range(3,360):
        jim.color(colors[i % len(colors)])  # Cycle through colors
        angle = 360/i
        for _ in range(i):
            jim.forward(100)
            jim.right(angle)


def randomwalk(jim, steps):
    angles = [0, 90, 180, 270, 360]
    jim.pensize(10)
    jim.speed("fastest")
    for _ in range(steps):
        anycolor()
        jim.setheading(random.choice(angles))
        jim.forward(50)
def anycolor():
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    c = (r,g,b)
    jim.color(c)
def many_cir():
    jim.speed("fastest")
    for _ in range(100):
        jim.setheading(random.randint(0,360))
        jim.circle(100)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        anycolor()
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)

col = colorgram.extract("img.jpg",10)
color = []
for i in col:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r,g,b)
    color.append(new_color)
if __name__ == "__main__":
    colors = ["blue", "green", "orange", "pink", "purple", "red", "violet", "yellow", "cyan", "magenta"]
    jim = Turtle()
    jim.speed("fastest")
    turtle.colormode(255)
    x= 10
    jim.penup()
    total_dots = 100

    for dot in range(1, total_dots + 1):
        jim.dot(20, random.choice(colors))
        jim.forward(50)

        if dot % 10 == 0:
            jim.setheading(90)
            jim.forward(50)
            jim.setheading(180)
            jim.forward(500)
            jim.setheading(0)
    screen = Screen()
    screen.exitonclick()

