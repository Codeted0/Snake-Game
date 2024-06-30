import time
from turtle import *
from food import Food
import random
from Snake import Snake
from score import Score

screen = Screen()
screensize(600, 600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() > 370 or snake.segments[0].xcor() < -370 or snake.segments[0].ycor() > 345 or \
            snake.segments[0].ycor() < -345:
        # game_is_on = False
        # score.game_over()
        snake.reset()
        score.reset()

    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment) < 10:
            # game_is_on = False
            score.reset()
            snake.reset()
            # score.game_over()
screen.exitonclick()


























