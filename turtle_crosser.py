from turtle import Turtle

class TurtleCrosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        # self.shapesize(2,2)
        self.speed("fastest")
       
        self.setheading(90)
        self.goto(0, -260)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())