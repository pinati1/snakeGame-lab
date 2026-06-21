import traceback
import turtle

from src.scoreboard import Scoreboard
from src.settings import *
from src.snake import Snake
from src.food import Food
from src.system_manager import SystemManager
import time
import tkinter


class Game:

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor(BG_COLOR)
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title("Snake")
        self.screen.tracer(0)
        self.snake = Snake()
        self.scoreboard = Scoreboard()
        self.food = Food()
        self.setup_bindings()
        self.system = SystemManager()
        self.pace = STARTING_SLEEP_DELAY
        self.stop = False

    def setup_bindings(self):
        self.screen.listen()

        controls = {
            "Up": self.snake.up,
            "Down": self.snake.down,
            "Left": self.snake.left,
            "Right": self.snake.right,
            "r": self.reset
        }

        for key, action in controls.items():
            self.screen.onkey(action, key)

    def run(self):
        try:
            while True:
                self.screen.update()
                time.sleep(self.pace)

                if self.stop:
                    continue

                self.system.update(self)

                if self.stop:
                    self.scoreboard.game_over()
                    self.scoreboard.save_high_score()
        except (turtle.Terminator, tkinter.TclError):
            pass

    def reset(self):
        if not self.stop:
            return
        self.snake.reset()
        self.food.refresh(self.snake.segments)
        self.scoreboard.reset()
        self.pace = STARTING_SLEEP_DELAY
        self.stop = False
