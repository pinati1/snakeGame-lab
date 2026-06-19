"""Scoreboard: owns the score number and knows how to draw it (and GAME OVER)."""

from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 18, "bold")
GAME_OVER_FONT = ("Courier", 28, "bold")


class Scoreboard:
    def __init__(self):
        self.score = 0
        # Composition: the scoreboard HAS-A pen it uses to write text.
        self.pen = Turtle()
        self.pen.hideturtle()   # don't show the arrow cursor
        self.pen.penup()        # don't draw lines while the pen moves
        self.pen.color("white")
        self.update_display()
    def reset(self):
        self.__init__()
    def update_display(self):
        """Redraw the score line at the top of the board."""
        self.pen.clear()
        self.pen.goto(0, 260)
        self.pen.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase_score(self, points=1):
        """Add points (default 1, but a banana gives 3, poison -2...) and redraw."""
        self.score += points
        self.update_display()

    def game_over(self):
        """Draw the GAME OVER message in the center of the board."""
        self.pen.goto(0, 0)
        self.pen.write("GAME OVER", align=ALIGN, font=GAME_OVER_FONT)
        self.pen.goto(0, -40)
        self.pen.write("Press 'r' to restart", align=ALIGN, font=FONT)

    def reset(self):
        """Zero the score for a new round (clears GAME OVER via update_display)."""
        self.score = 0
        self.update_display()