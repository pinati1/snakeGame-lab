import random
from turtle import Turtle
from src.settings import FOOD_OPTIONS, FOOD_X_BOUND, FOOD_Y_MIN, FOOD_Y_MAX, FOOD_SHAPE_STRETCH


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(FOOD_SHAPE_STRETCH, FOOD_SHAPE_STRETCH)
        self.penup()
        self.current_points = 1
        self.refresh()

    def is_on_snake(self, x, y, segments):
        for segment in segments:
            if abs(x - segment.xcor()) < 15 and abs(y - segment.ycor()) < 15:
                return True
        return False

    def refresh(self, segments=None):
        color, points = random.choice(FOOD_OPTIONS)
        self.color(color)
        self.current_points = points

        while True:
            random_x = random.randint(-FOOD_X_BOUND, FOOD_X_BOUND)
            random_y = random.randint(FOOD_Y_MIN, FOOD_Y_MAX)
            if segments is None or not self.is_on_snake(random_x, random_y, segments):
                break

        self.goto(random_x, random_y)
