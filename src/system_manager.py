from src.settings import *

try:
    import winsound
except ImportError:
    winsound = None


class System:
    """system interface"""
    def update(self, game):
        raise NotImplementedError


class SystemManager:
    def __init__(self):
        self.systems = [sys_class() for sys_class in System.__subclasses__()]

    def update(self, game):
        for system in self.systems:
            system.update(game)


class MovementSystem(System):
    def update(self, game):
        game.snake.move()


class EatingSystem(System):
    def update(self, game):
        if game.snake.head.distance(game.food) < 15:
            if winsound is not None:
                winsound.Beep(880, 401)
            game.scoreboard.increase_score(game.food.current_points)
            game.snake.grow()
            game.pace = max(MINIMUM_SLEEP_DELAY, game.pace - SPEED_INCREMENT)
            game.food.refresh(game.snake.segments)


class BorderSystem(System):
    def update(self, game):
        head = game.snake.head
        if abs(head.xcor()) > BORDER_X or abs(head.ycor()) > BORDER_Y:
            game.stop = True


class SnakeCollisionSystem(System):
    def update(self, game):
        head = game.snake.head
        for segment in game.snake.segments[1:]:
            if head.distance(segment) < 15:
                game.stop = True
