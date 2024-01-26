from turtle import Screen, Turtle
from turtle_crosser import TurtleCrosser
from obstacle import Obstacle
import time
from level_board import LevelBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

t_crosser = TurtleCrosser()
obstacles = Obstacle()
level = LevelBoard()

color_picker = ["red", "green", "white", "blue", "cyan", "orange"]
x_coordinates = [-350, -150, 0, 150, 350]
y_coordinates = [-180, 0, 180]
screen.onkeypress(key="Up", fun= t_crosser.move_up)
screen.onkeypress(key="Down", fun= t_crosser.move_down)
screen.onkeypress(key="Right", fun= t_crosser.move_right)
screen.onkeypress(key="Left", fun= t_crosser.move_left)


game_is_on = True
move_speed = 0.1

while game_is_on:
    time.sleep(move_speed)
    screen.update()
    obstacles.move_obstacles()

    ## Detect collision with obstacle
    for obstacle in obstacles.all_obstacles:
        if obstacle.distance(t_crosser) < 25:
            t_crosser.goto(0, -260)
            level.reset_level()
            move_speed = 0.1

    ## Turtle makes it across
    ## Return turtle to starting postion
    if t_crosser.ycor() > 280:
        t_crosser.goto(0, -260)
        level.increase_level()
        move_speed *= 0.9
        obstacles.create_obstacles()

screen.exitonclick()