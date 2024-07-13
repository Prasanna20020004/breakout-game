from turtle import Turtle
import random as rnd

COLORS = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'brown', 'cyan', 'magenta', 'lime']
X = -300
Y = 210


class Bricks:

    def __init__(self, n):
        self.bricks = []
        self.show_bricks(n)

    def show_bricks(self, number):
        global X, Y
        for i in range(int(number / 10)):
            for j in range(10):
                self.make_brick((X, Y))
                X += 65
            Y -= 25
            X = -300

    def make_brick(self, position):
        brick = Turtle("square")
        brick.color(rnd.choice(COLORS))
        brick.speed(0)
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(position)
        self.bricks.append(brick)

    def remove(self, brick):
        brick.goto(1000, 1000)
