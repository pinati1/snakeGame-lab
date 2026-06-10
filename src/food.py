"""Food entity: a circle that relocates (and recolors) after being eaten."""

import random
from turtle import Turtle

# Food stays on the 20px grid, fully inside the +/-288 border.
GRID_STEP = 20
BOUND = 280
FOOD_COLORS = ["red", "orange", "yellow", "cyan", "magenta", "lightgreen", "white"]


class Food(Turtle):
    """A small circular piece of food the snake tries to eat."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # ~10px circle
        self.speed(0)
        self.color("red")
        self.refresh([])

    def random_position(self, snake_segments):
        """Return a grid-aligned (x, y) that does not overlap any snake segment."""
        occupied = {(round(seg.xcor()), round(seg.ycor())) for seg in snake_segments}
        while True:
            x = random.randrange(-BOUND, BOUND + 1, GRID_STEP)
            y = random.randrange(-BOUND, BOUND + 1, GRID_STEP)
            if (x, y) not in occupied:
                return x, y

    def refresh(self, snake_segments):
        """Move the food to a new free location and give it a random color."""
        x, y = self.random_position(snake_segments)
        self.color(random.choice(FOOD_COLORS))
        self.goto(x, y)
