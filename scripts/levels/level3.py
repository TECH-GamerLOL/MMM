import pygame
from config import HEIGHT
from scripts.clouds import Clouds
from scripts.obstacle import Ground, Platform, MovingPlatform, Spikes
from scripts.levels.finish import Finish
from scripts.enemy import Snake, Eagle

class Level3:
    def __init__(self):
        self.width = 5500
        self.clouds = Clouds()
        self.obstacles = [
            Ground(0, HEIGHT - 50, 5500, 50),
            Platform(400, 500, 200, 20),
            MovingPlatform(800, 450, 150, 20, 3),
            Spikes(1200, HEIGHT - 70, 50, 20)
        ]
        self.enemies = []
        self.finish = Finish(5300, HEIGHT - 150)
        self.player_start_x = 400
        self.player_start_y = 150
        self.load_level()

    def load_level(self):
        self.obstacles.extend([
            Platform(1500, 350, 120, 20),
            Platform(1800, 300, 150, 20),
            MovingPlatform(2100, 250, 150, 20, 2),
            Spikes(2400, HEIGHT - 70, 50, 20),
            Platform(2700, 300, 150, 20),
            MovingPlatform(3100, 250, 120, 20, 3)
        ])

        self.enemies.extend([
            Snake(1000, HEIGHT - 100),
            Eagle(1700, 150),
            Snake(2500, HEIGHT - 100),
            Eagle(3200, 180),
            Snake(5000, HEIGHT - 100)
        ])

    def update(self, player):
        self.clouds.update()
        for enemy in self.enemies:
            if isinstance(enemy, Eagle):
                enemy.update(player)
            else:
                enemy.update(self.obstacles, player)
        for obstacle in self.obstacles:
            if hasattr(obstacle, 'update'):
                obstacle.update()

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
