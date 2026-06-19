from turtle import Turtle

# Constants for setup
from src.settings import *


class Snake:
    def __init__(self):
        """Initializes the snake with its starting segments and direction."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # The snake starts moving to the right automatically when the program starts
        self.head.setheading(RIGHT)
        self.direction = RIGHT
        self.next_direction = RIGHT
    def reset(self):
        """Resets the snake to its initial position."""
        for seg in self.segments:
            seg.hideturtle()
        self.__init__()
    def create_snake(self):
        """Creates the initial 3 segments of the snake."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a single 20x20 pixel segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("white")  # You can customize this if you add visual styling
        new_segment.penup()  # Prevents drawing lines when the turtle moves
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        """Adds a new segment to the end of the snake when food is eaten."""
        # Add the new segment at the position of the last segment in the list
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake continuously by 20 pixels."""
        # To move the nake properly, we move each segment to the position of the segment in front of it, starting from the tail.
        self.direction = self.next_direction
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(self.direction)
       # Finally, move the head forward by 20 pixels
        self.head.forward(MOVE_DISTANCE)

    # --- Directional Controls ---
    # Reverse movement is not allowed (e.g., if moving right, it cannot immediately move left)

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