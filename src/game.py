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
        self.draw_border()
        self.snake = Snake()
        self.scoreboard = Scoreboard()
        self.food = Food()
        for seg in self.snake.segments:
            seg.hideturtle()
        self.food.hideturtle()
        self.setup_bindings()
        self.system = SystemManager()
        self.pace = STARTING_SLEEP_DELAY
        self.stop = False
        self.started = False

    def draw_border(self):
        inset = -4
        half_width = SCREEN_WIDTH / 2 + inset
        half_height = SCREEN_HEIGHT /2 + inset
        corners = {

            'br': (half_width-5, -half_height+5),
            'tr': (half_width-5, half_height),
            'tl': (-half_width, half_height),
            'bl': (-half_width, -half_height+5),
        }

        border = turtle.Turtle()
        border.hideturtle()
        border.color("white")
        border.pensize(6)
        border.penup()
        border.goto(corners['bl'])
        border.pendown()
        for corner, point in corners.items():
            border.goto(point)

    def setup_bindings(self):
        self.screen.listen()

        controls = {
            "Up": self.snake.up,
            "Down": self.snake.down,
            "Left": self.snake.left,
            "Right": self.snake.right,
            "r": self.reset,
            "s": self.start
        }

        for key, action in controls.items():
            self.screen.onkey(action, key)

    def run(self):
        self.scoreboard.start_screen()
        try:
            while True:
                self.screen.update()
                time.sleep(self.pace)

                if self.stop or not self.started:
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

    def start(self):
        if self.started:
            return
        self.scoreboard.clear_message()
        for seg in self.snake.segments:
            seg.showturtle()
        self.food.showturtle()
        self.started = True
