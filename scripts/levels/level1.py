import pygame
from config import HEIGHT
from scripts.obstacle import Ground, Platform, MovingPlatform, Spikes
from scripts.levels.finish import Finish
from scripts.enemy import Snake, Eagle, GorillaBoss

class Level1:
    def __init__(self):
        self.width = 4000
        self.obstacles = [
            Ground(0, HEIGHT - 50, 3200, 50),
            Platform(100, 500, 200, 20),
            MovingPlatform(300, 400, 200, 20, 2),
            Spikes(600, 500, 50, 50)
        ]
        self.enemies = []  # <-- ADD THIS
        self.finish = Finish(2800, HEIGHT - 150)

        self.player_start_x = 400
        self.player_start_y = 150

        self.load_level()  # <-- ADD THIS so the extra platforms and enemies load

    def load_level(self):
        self.obstacles.append(Ground(0, 550, 1000, 50))
        self.obstacles.append(Platform(200, 450, 100, 20))
        self.obstacles.append(Platform(400, 350, 100, 20))
        self.obstacles.append(Spikes(600, 530, 50, 20))

        self.enemies.append(Snake(300, 500))
        self.enemies.append(Eagle(150, 300))
        self.enemies.append(GorillaBoss(700, 500))


    def update(self, player):
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
