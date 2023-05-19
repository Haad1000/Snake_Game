from turtle import Screen
import time
from snake import Snake
from food import  Food

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move_Snake()

    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()