from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280




class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.reached_finish_line = False

    def detect_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reached_finish_line = True
            self.goto(STARTING_POSITION)
        else:
            self.reached_finish_line = False

    def move(self):
        self.forward(MOVE_DISTANCE)

