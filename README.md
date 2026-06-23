# Snake Game

Ori Cohen, 211481791

Classic Snake made with Python and the `turtle` module.

## How to run

```
python main.py
```

Run it from the project root. The game opens in a 600x600 window. Press `s` to
start, arrow keys to steer, `r` to restart after a game over.

`highest_score.txt` lives in the project root and is created automatically the
first time you run the game if it isn't there already.

## Controls

| Key        | Action                   |
|------------|--------------------------|
| Arrow keys | Change direction         |
| s          | Start the game           |
| r          | Restart after game over  |

The snake moves on its own once started; you only pick the direction, and it
can't turn 180 degrees on itself (e.g. pressing left while moving right does
nothing).

## Project structure

```
main.py                 # entry point
src/
  game.py               # screen setup, game loop, bindings
  system_manager.py     # movement / eating / collision logic
  snake.py              # Snake class
  food.py               # Food class
  scoreboard.py         # Scoreboard class, score file handling
  settings.py           # constants (sizes, speeds, colors)
```

## Test scenarios

1. **Eating food** - started the game and steered the snake into a piece of
   food. The snake grew by one segment, the score went up by the food's point
   value (1/3/5 depending on color), the food jumped to a new random spot, and
   the game got slightly faster.

2. **Reversing direction** - while the snake was moving right, pressed the
   left arrow key. The snake kept moving right instead of reversing into
   itself, since that move is blocked.

3. **Game over and score saving** - drove the snake into the border. The game
   stopped, "GAME OVER" was shown on screen, and the score was written to
   `highest_score.txt` since it was higher than what was stored there. Pressed
   `r` afterward and the game reset back to 3 segments, score 0, original
   speed.
