from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(320,260)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score}",align="center",font = ("Arial",20,"normal"))
        self.score += 1

    def game_over(self):
        self.goto(0,70)
        self.write("Game Over",align="center",font = ("Arial",20,"normal"))
