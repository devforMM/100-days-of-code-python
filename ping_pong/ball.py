from turtle import Turtle
import random 
import time
W=400
H=290
class Ball(Turtle):
    def __init__(self ) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("red")
        self.speed("slowest")
        self.penup()
            
    def random_move(self):
        global W,H
        x=random.choice([-350,350])
        y=random.randint(-290,290)
        self.goto(x,y)
    def move_left(self):
        x=-350
        y=random.randint(-290,290)
        self.goto(x,y)
    def move_right(self):
        x=+350
        y=random.randint(-290,290)
        self.goto(x,y)
    def home(self):
        self.goto(0,0)
        time.sleep(1)
        
    def check_collision(self, paddle):
     return self.distance(paddle) < 20

            
            
        