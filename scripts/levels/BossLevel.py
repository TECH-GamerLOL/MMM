import pygame
from config import HEIGHT
from scripts.clouds import Clouds
from scripts.obstacle import Ground, Platform, MovingPlatform, Spikes
from scripts.levels.finish import Finish
from scripts.enemy import Snake, Eagle, GorillaBoss

class FinalBossLevel:
    def __init__(self):
        self.width = 7000
        self.clouds = Clouds()
        self.obstacles = [
            Ground(0, HEIGHT - 50, 7000, 50),
            Platform(500, 500, 200, 20),
            MovingPlatform(1000, 450, 150, 20, 3),
            Spikes(1400, HEIGHT - 70, 50, 20)
        ]
        self.enemies = []
        self.finish = Finish(6800, HEIGHT - 150)
        self.player_start_x = 400
        self.player_start_y = 150
        self.load_level()

    def load_level(self):
        self.obstacles.extend([
            Platform(1800, 350, 120, 20),
            Platform(2100, 300, 150, 20),
            MovingPlatform(2500, 250, 120, 20, 2),
            Spikes(2900, HEIGHT - 70, 50, 20),
            Platform(3300, 300, 150, 20),
            MovingPlatform(3700, 250, 150, 20, 3)
        ])

        self.enemies.extend([
            Snake(1700, HEIGHT - 100),
            Eagle(2300, 150),
            Snake(3000, HEIGHT - 100),
            Eagle(3400, 180),
            GorillaBoss(6400, HEIGHT - 200)  # Final boss enemy
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