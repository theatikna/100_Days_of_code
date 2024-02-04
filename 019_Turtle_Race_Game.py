import random
from turtle import Turtle, Screen

# Create a screen
screen = Screen()
screen.setup(width=700, height=500)
colors = ["red", "green", "black", "yellow", "blue"]
all_name = ["tim", "jim", "kim", "him", "tom"]

# Map each turtle to its name using a dictionary
turtle_dict = dict(zip(all_name, [Turtle(shape="turtle") for _ in range(5)]))

x = -230
y = 0
user = screen.textinput(title="Enter The Bet", prompt="Enter The Turtle Color")
user_guess = Turtle()
user_guess.penup()
user_guess.goto(250, 70)
user_guess.write(f"Your Choice: {user}", align="left")

for t, (name, turtle) in enumerate(turtle_dict.items()):
    turtle.color(colors[t])
    turtle.penup()
    turtle.goto(x, 40 * t)

winner_found = False
while not winner_found:
    for turtle in turtle_dict.values():
        turtle.forward(random.randint(10, 30))
        if turtle.xcor() > 230:
            winner_found = True
            winning_turtle = turtle
            break

# Display the winner's color and outcome
user_guess.clear()
user_guess.goto(250, 70)
user_guess.write(f"Winner: {winning_turtle.color()[0]}", align="left")

if winning_turtle.color()[0].lower() == user.lower():
    user_guess.goto(100, 70)
    user_guess.write("You Won!", align="center")
else:
    user_guess.goto(100, 70)
    user_guess.write("Better Luck Next Time", align="center")

# Close the screen when clicked
screen.exitonclick()
