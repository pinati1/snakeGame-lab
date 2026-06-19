from src.settings import *



class System:
    """system interface"""

    def update(self, game):
        raise NotImplementedError


class SystemManager:
    def __init__(self):
        self.systems = [sys_class() for sys_class in System.__subclasses__()]

    def update(self, game):
        """Runs the update method on every dynamically loaded system."""
        for system in self.systems:
            system.update(game)


class MovementSystem(System):
    def update(self, game):
        game.snake.move()


class EatingSystem(System):
    def update(self, game):
        if game.snake.head.distance(game.food) < 15:
            game.scoreboard.increase_score()
            game.snake.grow()
            game.pace = max(MINIMUM_SLEEP_DELAY, game.pace - SPEED_INCREMENT)
            game.food.refresh()


class BorderSystem(System):
    def update(self, game):
        head = game.snake.head
        if abs(head.xcor()) > BORDER_LIMIT or abs(head.ycor()) > BORDER_LIMIT:
            game.stop = True


class SnakeCollisionSystem(System):
    def update(self, game):
        head = game.snake.head
        for segment in game.snake.segments[1:]:  # skip [0] — that's the head itself
            if head.distance(segment) < 15:
                game.stop = True
