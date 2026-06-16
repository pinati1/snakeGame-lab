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
        # To move the snake properly, we move each segment to the position of the segment in front of it, starting from the tail.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Finally, move the head forward by 20 pixels
        self.head.forward(MOVE_DISTANCE)

    # --- Directional Controls ---
    # Reverse movement is not allowed (e.g., if moving right, it cannot immediately move left)

    def up(self):
        """Changes direction to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes direction to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes direction to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes direction to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)