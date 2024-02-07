from turtle import Screen
from player import Player
import time
from car_manager import Car
from scoreboard import Scoreboard

# Create Screen
screen = Screen()
screen.tracer(0)
screen.setup(800, 600)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up_move, "Up")
screen.onkey(player.right_move, "Right")
screen.onkey(player.left_move, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.car_move()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check collision with player
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increse_level()

    screen.update()  # Update screen after all changes

screen.exitonclick()
