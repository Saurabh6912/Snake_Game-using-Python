from screen_structure import *
# “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
starting_pos = [(-20,0),(-40,0)]
moving_pos = 20
class Snake:
    def __init__(self):
        self.head = t.Turtle(shape='square')
        self.head.color('red')
        self.head.fillcolor("goldenrod4")
        self.head.shapesize(0.85,0.8,0.7)
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        self.segments.append(self.head)
        for position in starting_pos:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = t.Turtle(shape='square')
        new_segment.color('gray1')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.penup()
        self.head.forward(moving_pos)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
