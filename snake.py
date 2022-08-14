from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40, 0)]
MOVE_DISTANCE = 20
COLOR = "white"

class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):    
        for pos in POSITIONS:
            self.add_segment(pos)
    
    def add_segment(self, position):
        newt = Turtle("square")
        newt.color(COLOR)
        newt.penup()
        newt.goto(position)
        self.segments.append(newt)

    def extends(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto((1000,1000))
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            self.segments[seg].goto(self.segments[seg-1].pos())
        self.segments[0].forward(MOVE_DISTANCE)
    
    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def posX(self):
        return self.head.xcor()
    
    def posY(self):
        return self.head.ycor()


