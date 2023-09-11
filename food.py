from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1.2,stretch_wid=1.2)
        self.color('green1')
        self.fillcolor('orange')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)