"""Snake entity: builds the body, moves it, grows it and controls its direction."""

from turtle import Turtle

# Movement and layout constants.
MOVE_DISTANCE = 20
SEGMENT_SIZE = 20  # each Turtle square is 20 x 20 pixels
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Heading angles used by Turtle (degrees).
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """The player-controlled snake made of square Turtle segments."""

    def __init__(self):
        self.segments = []
        self.create_body()

    def create_body(self):
        """Create the initial three-segment snake at the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create a single white square segment at the given position."""
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.speed(0)
        segment.goto(position)
        self.segments.append(segment)

    @property
    def head(self):
        """The first segment, used for collision and direction checks."""
        return self.segments[0]

    def grow(self):
        """Add a new segment at the current tail position (after eating food)."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward: each segment follows the one ahead of it."""
        for index in range(len(self.segments) - 1, 0, -1):
            ahead = self.segments[index - 1].position()
            self.segments[index].goto(ahead)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        """Send old segments off-screen and rebuild a fresh three-segment snake."""
        for segment in self.segments:
            segment.goto(1000, 1000)
            segment.hideturtle()
        self.segments = []
        self.create_body()

    # --- Direction controls (reverse movement is blocked) ---
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
