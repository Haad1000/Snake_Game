from turtle import Turtle
Alignment = "center"
Font = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.updateScore()
        self.hideturtle()

    def updateScore(self):
        self.write(f"Score: {self.score}", True, align=Alignment, font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.updateScore()