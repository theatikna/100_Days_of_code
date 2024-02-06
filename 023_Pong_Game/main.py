from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_ball = Ball()
scoreboard = Scoreboard()
scoreboard.line()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")

game_is_on = True
while game_is_on:
    time.sleep(game_ball.ball_speed)
    screen.update()
    game_ball.move()
    # Detect Collision with Wall
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()
    # Detect Collision with Paddle
    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320:
        game_ball.bounce_x()
    elif game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()
    # R_Paddle Misses the ball
    if game_ball.xcor() > 380:
        game_ball.reset_game()
        scoreboard.lscore()
    if game_ball.xcor() < -380:
        game_ball.reset_game()
        scoreboard.rscore()
screen.exitonclick()
