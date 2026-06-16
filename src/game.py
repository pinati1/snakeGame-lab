import turtle
from src.settings import *
from src.snake import Snake
from src.food import Food
import time

class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor(BG_COLOR)
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title("Snake")
        self.snake = Snake()
        self.food = Food(self.screen)
        self.setup_bindings()

        self.stop = False

    def setup_bindings(self):
        """Registers all keyboard listeners using a dictionary mapping."""
        self.screen.listen()

        # Map the Key string to the Function
        controls = {
            "Up": self.snake.up,
            "Down": self.snake.down,
            "Left": self.snake.left,
            "Right": self.snake.right
        }

        # Loop through the dictionary and bind them automatically
        for key, action in controls.items():
            self.screen.onkey(action, key)

    def run(self):
        # self.food.refresh()
        while not self.stop:
            self.screen.update()
            time.sleep(0.1)  # Add this to slow the game down
            self.snake.move()
