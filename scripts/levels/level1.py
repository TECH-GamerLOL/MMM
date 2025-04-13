import pygame
from config import HEIGHT
from scripts.clouds import Clouds
from scripts.obstacle import Ground, Platform, MovingPlatform, Spikes
from scripts.levels.finish import Finish
from scripts.enemy import Snake, Eagle, GorillaBoss

class Level1:
    def __init__(self):
        self.width = 4000
        self.clouds = Clouds()
        self.obstacles = [
            Ground(0, HEIGHT - 50, 4000, 50),
            Platform(100, 500, 200, 20),
            MovingPlatform(300, 400, 200, 20, 2),
            Spikes(600, 500, 50, 50)
        ]
        self.enemies = []  # <-- ADD THIS
        self.finish = Finish(3800, HEIGHT - 150)

        self.player_start_x = 400
        self.player_start_y = 150

        self.load_level()  # <-- ADD THIS so the extra platforms and enemies load

    def load_level(self):
        self.obstacles.append(Platform(800, 450, 120, 20))
        self.obstacles.append(Platform(1000, 350, 120, 20))
        self.obstacles.append(Platform(1300, 300, 150, 20))
        self.obstacles.append(Platform(1600, 250, 120, 20))
        self.obstacles.append(MovingPlatform(1900, 400, 150, 20, 3))
        self.obstacles.append(Spikes(2200, HEIGHT - 70, 50, 20))
        self.obstacles.append(Spikes(2400, HEIGHT - 70, 50, 20))

        self.enemies.append(Snake(500, HEIGHT - 100))
        self.enemies.append(Snake(1500, HEIGHT - 100))
        self.enemies.append(Eagle(1800, 200))
        self.enemies.append(GorillaBoss(3600, HEIGHT - 150))


    def update(self, player):
        self.clouds.update()
        for enemy in self.enemies:
            if isinstance(enemy, Eagle):
                enemy.update(player)  # Eagle ignores obstacles
            else:
                enemy.update(self.obstacles, player)

        for obstacle in self.obstacles:
            if hasattr(obstacle, 'update'):
                obstacle.update()

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)  # Placeholder for cloud visuals

        for obstacle in self.obstacles:
            obstacle.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)
