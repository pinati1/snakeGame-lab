import glob
import random
from turtle import Turtle
from settings import POINT_SYSTEM

ALL_GIFS = glob.glob("../assets/food_gifs/*.gif")



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_points = 1  # A safe default
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