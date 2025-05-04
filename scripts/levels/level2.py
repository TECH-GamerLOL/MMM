import pygame
from config import HEIGHT
from scripts.clouds import Clouds
from scripts.obstacle import Ground, Platform, MovingPlatform, Spikes
from scripts.levels.finish import Finish
from scripts.enemy import Snake, Eagle

class Level2:
    def __init__(self):
        self.width = 5000
        self.clouds = Clouds()
        self.obstacles = [
            Ground(0, HEIGHT - 50, 5000, 50),
            Platform(200, 500, 150, 20),
            MovingPlatform(600, 400, 200, 20, 3),
            Spikes(1000, 550, 50, 30),
        ]
        self.enemies = []
        self.finish = Finish(4800, HEIGHT - 150)
        self.player_start_x = 400
        self.player_start_y = 150
        self.load_level()

    def load_level(self):
        self.obstacles += [
            Platform(1200, 450, 100, 20),
            Platform(1400, 400, 100, 20),
            MovingPlatform(1700, 350, 200, 20, 2),
            Platform(2000, 300, 120, 20),
            Spikes(2200, HEIGHT - 70, 50, 20),
            Spikes(2250, HEIGHT - 70, 50, 20)
        ]
        self.enemies += [
            Snake(800, HEIGHT - 100),
            Snake(1600, HEIGHT - 100),
            Eagle(1900, 200),
            Snake(2500, HEIGHT - 100)
        ]

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
