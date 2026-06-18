"""Snake Game with Turtle.

Initializes the screen, wires up keyboard listeners and runs the main game loop.
Includes bonus features: a start screen, a restart option and colored food.
"""

import time
import turtle
from turtle import Screen, Turtle

from src.snake import Snake
from src.food import Food
from src.scoreboard import Scoreboard

# Speed control (sleep delay in seconds between movement steps).
DELAY_START = 0.1
DELAY_MIN = 0.05
DELAY_STEP = 0.01

# Border limit: the head fails when it crosses +/-288 on either axis.
BORDER_LIMIT = 288

# Screen setup.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn off auto-refresh so we can update manually

# Game objects.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Simple flags toggled by keyboard callbacks.
game_started = False
restart_requested = False


def begin():
    """Callback: leave the start screen and begin playing."""
    global game_started
    game_started = True


def request_restart():
    """Callback: ask the loop to start a fresh game after GAME OVER."""
    global restart_requested
    restart_requested = True


# Register keyboard listeners (arrows only control the snake's direction).
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(begin, "space")
screen.onkey(request_restart, "r")


def show_start_screen():
    """Display the title screen and wait for the player to press Space."""
    global game_started
    game_started = False
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("white")
    pen.goto(0, 40)
    pen.write("SNAKE", align="center", font=("Courier", 48, "bold"))
    pen.goto(0, -20)
    pen.write("Press Space to Start", align="center", font=("Courier", 20, "normal"))
    pen.goto(0, -60)
    pen.write("Arrow keys to steer", align="center", font=("Courier", 14, "normal"))
    while not game_started:
        screen.update()
        time.sleep(0.05)
    pen.clear()


def wait_for_restart():
    """After GAME OVER, wait until the player presses 'r'."""
    global restart_requested
    restart_requested = False
    while not restart_requested:
        screen.update()
        time.sleep(0.05)


def handle_game_over():
    """Save the high score (only if beaten) and show the GAME OVER message."""
    if scoreboard.score > scoreboard.read_highest_score():
        scoreboard.save_highest_score()
    scoreboard.game_over()
    screen.update()


def play_round():
    """Run a single game until the snake hits a border or its own tail."""
    delay = DELAY_START
    game_on = True
    while game_on:
        screen.update()
        time.sleep(delay)
        snake.move()

        # Eat food: relocate/recolor it, grow, score up and speed up.
        if snake.head.distance(food) < 15:
            food.refresh(snake.segments)
            snake.grow()
            scoreboard.increase_score()
            delay = max(DELAY_MIN, round(delay - DELAY_STEP, 2))

        # Border collision.
        head = snake.head
        if (head.xcor() > BORDER_LIMIT or head.xcor() < -BORDER_LIMIT
                or head.ycor() > BORDER_LIMIT or head.ycor() < -BORDER_LIMIT):
            game_on = False

        # Tail collision.
        for segment in snake.segments[1:]:
            if head.distance(segment) < 15:
                game_on = False
                break

    handle_game_over()


def main():
    """Top-level flow: start screen, then play/restart rounds forever."""
    show_start_screen()
    while True:
        snake.reset()
        scoreboard.reset()
        food.refresh(snake.segments)
        play_round()
        wait_for_restart()


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        # The player closed the window; no special save is required.
        pass
