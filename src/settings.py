# settings.py

# ============================================================
# Primary knobs — change these and the whole layout adapts.
# ============================================================
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BG_COLOR = "black"
TITLE = "My Snake Game"

# ============================================================
# Fixed game rules (spec-mandated — these do NOT scale with the screen).
# ============================================================
SEGMENT_SIZE = 20                 # each snake square / food cell is 20x20 px
MOVE_DISTANCE = SEGMENT_SIZE      # one movement step = one cell

STARTING_POSITIONS = [(0, 0), (-SEGMENT_SIZE, 0), (-2 * SEGMENT_SIZE, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# ============================================================
# Layout — all derived from the screen size above.
# ============================================================
WALL_MARGIN = 12                                   # inset between the window edge and the wall
BORDER_X = SCREEN_WIDTH // 2 - WALL_MARGIN          # 288 at 600 wide
BORDER_Y = SCREEN_HEIGHT // 2 - WALL_MARGIN         # 288 at 600 tall

SCORE_MARGIN = 40                                  # gap from the top wall down to the score text
SCORE_Y = SCREEN_HEIGHT // 2 - SCORE_MARGIN        # 260 at 600 tall

_HALF_SEGMENT = SEGMENT_SIZE // 2                   # keep food fully inside the wall
FOOD_X_BOUND = BORDER_X - _HALF_SEGMENT            # horizontal spawn limit (both sides)
FOOD_Y_MIN = -(BORDER_Y - _HALF_SEGMENT)          # bottom spawn limit
FOOD_Y_MAX = SCORE_Y - SEGMENT_SIZE                # top spawn limit — stays below the score text
SAFE_GAP = SEGMENT_SIZE                            # min distance food keeps from any snake segment

# ============================================================
# Game speed.
# ============================================================
STARTING_SLEEP_DELAY = 0.13
MINIMUM_SLEEP_DELAY = 0.05
SPEED_INCREMENT = 0.01

# ============================================================
# Food point values.
# ============================================================
POINT_SYSTEM = {
    "apple": 1,
    "pineapple": 3,
    "watermelon": 5,
    "poison": -2,
}
