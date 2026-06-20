# settings.py

# Screen Settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"
TITLE = "My Snake Game"

# Snake Settings
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Game Speed
STARTING_SLEEP_DELAY = 0.13
MINIMUM_SLEEP_DELAY = 0.05
SPEED_INCREMENT = 0.01
BORDER_LIMIT =288

#Food point values
POINT_SYSTEM = {
    "apple": 10,
    "pineapple": 3,
    "watermelon": 5,
    "poison": -2
}