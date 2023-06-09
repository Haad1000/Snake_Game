from turtle import Turtle

move_Speed = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.parts = []
        self.create_Snake()
        self.head = self.parts[0]

    def create_Snake(self):
        for i in range(3):
            self.extend_snake()

    def extend_snake(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        self.parts.append(tim)

    def bite_eaten(self):
        self.extend_snake()
        self.parts[len(self.parts) - 1].goto(self.parts[len(self.parts) - 2].xcor(), self.parts[len(self.parts) - 2].ycor())

    def move_Snake(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i - 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(move_Speed)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.seth(RIGHT)