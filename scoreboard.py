from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.display()

    def display(self):
        self.clear()  # Clear previous score display
        self.goto(0, 240)  # Position the turtle to write the score
        self.write(f"Score: {self.score}", align="center", font=("Courier", 30, "bold"))

    def update_score(self):
        self.score += 1

    def display_end_score(self):
        self.clear()  # Clear previous score display
        self.goto(0, 0)  # Position the turtle to write the score
        self.write(f"Score: {self.score}", align="center", font=("Courier", 30, "bold"))
