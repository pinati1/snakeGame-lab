"""Scoreboard: shows the current and highest score and the GAME OVER message."""

import os
from turtle import Turtle

# Keep the high-score file in the project root (parent of this src/ folder),
# so it is found no matter which directory the game is launched from.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCORE_FILE = os.path.join(PROJECT_ROOT, "highest_score.txt")
ALIGNMENT = "center"
FONT = ("Courier", 18, "bold")
GAME_OVER_FONT = ("Courier", 28, "bold")


class Scoreboard(Turtle):
    """Displays scores at the top and handles persistent high-score storage."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highest_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def read_highest_score(self):
        """Load the high score, creating the file with 0 if it is missing/invalid."""
        if not os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "w") as file:
                file.write("0")
            return 0
        try:
            with open(SCORE_FILE, "r") as file:
                return int(file.read().strip())
        except (ValueError, OSError):
            return 0

    def save_highest_score(self):
        """Persist the current high score to disk."""
        with open(SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def update_score(self):
        """Redraw the score line at the top center of the board."""
        self.clear()
        self.goto(0, 260)
        self.write(
            f"Your Score: {self.score}   Highest Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """Add one point and update the high score live if it was beaten."""
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def game_over(self):
        """Show a visible GAME OVER message in the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -40)
        self.write("Press 'r' to restart", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the current score for a new round (keeps the high score)."""
        self.score = 0
        self.update_score()
