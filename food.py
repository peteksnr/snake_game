from turtle import Turtle
import random


class Food(Turtle):  # food class inherits from turtle class
    def __init__(self):
        super().__init__()  # we inherit turtle's init function
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # we created 10x10 circle
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
