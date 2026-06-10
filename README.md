# Snake Game (Python + Turtle)

Classic Snake built from scratch with the standard-library `turtle` module, using an
object-oriented design.

## How to run

```
python src/main.py
```

Run it from the project root. `highest_score.txt` is created in the project root automatically.
Requires Python 3 with `turtle` (included in the standard library; on Linux it needs `tkinter`).

## Controls

| Key         | Action                  |
|-------------|-------------------------|
| Arrow keys  | Change direction        |
| Space       | Start the game          |
| r           | Restart after GAME OVER |

The snake moves on its own and starts heading right. You can only change its
direction — and it cannot reverse straight back on itself.

## How it works

The code lives in `src/`, one class per file:

- `src/snake.py` — `Snake`: builds the 3-segment body, `move()`, `grow()`, direction
  methods (`up/down/left/right`) that block 180° reversals, and `reset()` for restarts.
- `src/food.py` — `Food`: a circle that calls `refresh()` to jump to a random free grid
  cell (never on the snake) and pick a random color.
- `src/scoreboard.py` — `Scoreboard`: draws the current and highest score at the top,
  shows GAME OVER, and loads/saves the high score from `highest_score.txt`.
- `src/main.py` — screen setup, keyboard listeners and the main game loop.

### Rules implemented
- 600×600 board, ±288 border limit, 20px segments and steps.
- Eating food (`distance < 15`) grows the snake, adds 1 point, and speeds the game up
  (sleep delay 0.1s → −0.01 per food, floored at 0.05s).
- The high score updates live and is saved on failure only when it beats the stored value.
- Failure on hitting a border or the snake's own tail shows a visible GAME OVER.

### Bonus features
- Start screen before the game begins.
- Restart with `r` after GAME OVER.
- Randomly colored food.
