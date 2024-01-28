import turtle

def move_turtle(x, y):
    tim.setheading(tim.towards(x, y))
    tim.goto(x,y)

tim = turtle.Turtle()
screen = turtle.Screen()

tim.shape("turtle")
tim.color("red", "green")

# Set up the onclick event to call the move_turtle function
screen.onscreenclick(move_turtle)

# Keep the window open until the user closes it
screen.mainloop()
