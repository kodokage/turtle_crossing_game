from turtle import Turtle
import time

class LevelBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        self.color("white")
        self.penup()
        self.update_level()
        
        # self.goto(0, 260)
        # self.write(self.level, align="center", font=("Arial", 20, "normal"))

    def update_level(self):
        self.clear()
        self.goto(0, 260)
        self.write("Level " + str(self.level), align="center", font=("Arial", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def reset_level(self):
        self.level = 0
        self.update_level()
