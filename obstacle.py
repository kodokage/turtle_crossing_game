from turtle import Turtle
import random

color_picker = ["red", "green", "white", "blue", "cyan", "orange"]
x_coordinates = [-350, -150, 0, 150, 350]
# y_coordinates = [-180, 0, 180]

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.all_obstacles = []
        self.create_obstacles()

    def create_obstacles(self):
        for obstacle in range (20):
            obstacle = Turtle("square")
            obstacle.penup()
            obstacle.shapesize(1,2)
            obstacle.color(random.choice(color_picker))
            self.x_location = random.choice(x_coordinates)
            # self.y_location = random.choice(y_coordinates)
            self.y_location = random.randint(-200, 200)
            obstacle.goto(self.x_location, self.y_location)
            self.all_obstacles.append(obstacle)

    def move_obstacles(self):
        for obstacle in self.all_obstacles:
            obstacle.setheading(180)
            obstacle.forward(10)
            
            if obstacle.xcor() < -400:
                obstacle.goto(340, obstacle.ycor())



