from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()
score_Board = ScoreBoard()

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
        score_Board.increase_score()
        snake.bite_eaten()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_Board.game_over()
        game_on = False

    for parts in snake.parts:
        if parts == snake.head:
            pass
        else:
            if snake.head.distance(parts) < 10:
                score_Board.game_over()
                game_on = False

screen.exitonclick()