from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.x=x
        self.y=y
        self.penup()
        self.goto(x,y)
        self.write (self.score ,font=("Arial",22,"normal"))
        self.hideturtle()
    def update_score(self):
        self.write(self.score,font=("Arial",22,"normal"))    
    
    def increase(self):
        self.score+=1
        self.clear()
        self.update_score()
        
    