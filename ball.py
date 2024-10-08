from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.speed(1)

    def move(self):
        x = self.xcor() - self.x_move
        y = self.ycor() - self.y_move
        self.teleport(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
