import glob
import random
from turtle import Turtle
from src.settings import POINT_SYSTEM

ALL_GIFS = glob.glob("assets/food_gifs/*.gif")


class Food(Turtle):
    # 1. Add 'screen' inside the parentheses
    def __init__(self, screen):
        super().__init__()
        self.penup()

        # 2. Register all the shapes with the screen right away
        if ALL_GIFS:
            for gif in ALL_GIFS:
                screen.addshape(gif)

        self.current_points = 1
        self.refresh()

    def refresh(self):
        """Moves the food, picks a random GIF, and calculates its value."""

        if ALL_GIFS:
            # 1. Pick a random image from the massive list of GIFs
            random_image = random.choice(ALL_GIFS)
            self.shape(random_image)

            # 2. Determine the points using substring matching
            self.current_points = 1  # Reset to default just in case it's an unknown fruit

            for keyword, points in POINT_SYSTEM.items():
                if keyword in random_image:  # E.g., if "apple" is in "red_apple_2.gif"
                    self.current_points = points
                    break  # We found the match, stop searching the dictionary

        else:
            # Fallback if no GIFs exist
            self.shape("circle")
            self.color("red")
            self.current_points = 1

        # 3. Move to a random location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)