from turtle import Turtle
import random
class Padle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.width = 5
        self.height = 1
        self.x = x
        self.y = y
        self.create_padle()
         

    def create_padle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(self.width, self.height)
        self.penup()
        self.goto(self.x, self.y)


         
        