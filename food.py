from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x_position = random.randint(-350, 350)
        y_position = random.randint(-320, 320)
        self.goto(x_position, y_position)
