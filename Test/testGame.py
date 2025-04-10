import sys
import os
import pygame

# Add the 'scripts' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

# Now you can import from the 'scripts' folder
from clouds import Clouds
from player import Menkey
from enemy import Enemy
from collision import check_collision
from obstacle import Platform, MovingPlatform, Spikes, Ground
from config import WIDTH, HEIGHT


class DummyDashboard:
    def __init__(self):
        self.points = 0
        self.coins = 0

class DummyLevel:
    def __init__(self):
        self.entityList = []

class DummySound:
    def play_sfx(self, sound): pass
    coin = None
    pipe = None

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menkey Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.BLUE = (0, 255, 255)

        self.clouds = Clouds()

        # Dummy instances
        self.dashboard = DummyDashboard()
        self.level = DummyLevel()
        self.sound = DummySound()

        self.player = Menkey(400, 150, self.level, self.dashboard, self.sound, self.screen)
        self.enemy = Enemy(400, 150)

        self.obstacles = [
            Ground(0, HEIGHT - 50, WIDTH, 50),
            Platform(100, 500, 200, 20),
            MovingPlatform(300, 400, 200, 20, 2),
            Spikes(600, 500, 50, 50)
        ]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.clouds.update()
        self.player.update(self.obstacles)
        self.enemy.update(self.obstacles)
        self.enemy.move()

        for obstacle in self.obstacles:
            if isinstance(obstacle, MovingPlatform):
                obstacle.update()

        if check_collision(self.player, self.enemy):
            self.player.takeDamage(10)
            print("Player collided with enemy")

        for obstacle in self.obstacles:
            if isinstance(obstacle, Spikes):
                if self.player.rect.colliderect(obstacle.rect):
                    self.player.takeDamage(10)
                    print("Player collided with spikes")

    def render(self):
        self.screen.fill(self.BLUE)
        self.clouds.render(self.screen)
        self.player.draw(self.screen)
        self.player.draw_health(self.screen)
        self.enemy.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        pygame.display.update()
