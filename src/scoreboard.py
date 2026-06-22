from turtle import Turtle
from pathlib import Path
from src.settings import SCORE_Y


ALIGN = "center"
FONT = ("Courier", 18, "bold")
GAME_OVER_FONT = ("Courier", 28, "bold")
HIGHSCORE_FILE = Path("highest_score.txt")


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = self.read_highest_score()
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color("white")
        self.message_pen = Turtle()
        self.message_pen.hideturtle()
        self.message_pen.penup()
        self.message_pen.color("white")
        self.update_display()

    def update_display(self):
        self.pen.clear()
        self.pen.goto(0, SCORE_Y)
        self.pen.write(f"Score: {self.score}      Highest Score:{self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self, points=1):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_display()

    def game_over(self):
        self.message_pen.goto(0, 0)
        self.message_pen.write("GAME OVER", align=ALIGN, font=GAME_OVER_FONT)
        self.message_pen.goto(0, -40)
        self.message_pen.write("Press 'r' to restart", align=ALIGN, font=FONT)

    def start_screen(self):
        self.message_pen.goto(0, 0)
        self.message_pen.write("snake", align=ALIGN, font=FONT)
        self.message_pen.goto(0, -40)
        self.message_pen.write("for start press 's'", align=ALIGN, font=FONT)

    def clear_message(self):
        self.message_pen.clear()

    def reset(self):
        self.score = 0
        self.update_display()
        self.clear_message()

    def read_highest_score(self):
        if not HIGHSCORE_FILE.exists():
            HIGHSCORE_FILE.write_text("0")
            return 0
        try:
            return int(HIGHSCORE_FILE.read_text().strip())
        except ValueError:
            return 0

    def save_high_score(self):
        HIGHSCORE_FILE.write_text(str(self.high_score))
