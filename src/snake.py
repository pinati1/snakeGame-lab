from turtle import Turtle
from src.settings import *


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(RIGHT)
        self.direction = RIGHT
        self.next_direction = RIGHT

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.__init__()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        self.direction = self.next_direction
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(self.direction)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.direction != DOWN:
            self.next_direction = UP

    def down(self):
        if self.direction != UP:
            self.next_direction = DOWN

    def left(self):
        if self.direction != RIGHT:
            self.next_direction = LEFT

    def right(self):
        if self.direction != LEFT:
            self.next_direction = RIGHT
