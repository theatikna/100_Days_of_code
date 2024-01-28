import turtle

def move_turtle(x, y):
    tim.setheading(tim.towards(x, y))
    tim.goto(x, y)

def circle(x, y):  # Adjust the circle function to accept x, y parameters
    tim.penup()      # Lift the pen before moving to the center
    tim.goto(x, y)   # Move to the center of the circle
    tim.pendown()    # Put the pen down before drawing
    tim.circle(20)   # Draw the circle

tim = turtle.Turtle()
screen = turtle.Screen()

tim.shape("turtle")
tim.color("red", "green")

mode = input("Enter the Mode: ").lower()

# Set up the onclick event based on user input
if mode == "move":
    screen.onscreenclick(move_turtle)
elif mode == "circle":
    screen.onscreenclick(circle)

# Keep the window open until the user closes it
screen.mainloop()
