import pygame
from core.player import Menkey
from core.enemy import Enemy
from core.collision import check_collision
from core.obstacle import Platform, MovingPlatform, Spikes, Ground
from config import WIDTH, HEIGHT

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print("Initialising game")
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menkey Game")

WHITE = (255, 255, 255)

player = Menkey(400, 150)
enemy = Enemy(400,150)  
obstacles = [
    Ground(0, HEIGHT - 50, WIDTH, 50),
    Platform(100, 500, 200, 20),
    MovingPlatform(300, 400, 200, 20, 2),
    Spikes(600, 500, 50, 50)
]

running = True
clock = pygame.time.Clock()

while running:
    print("Game loop running")
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(obstacles)
    player.draw(screen)
    player.draw_health(screen)

    enemy.update(obstacles)
    enemy.move()  
    enemy.draw(screen)

    for obstacle in obstacles:
        if isinstance(obstacle, MovingPlatform):
            obstacle.update()
        obstacle.draw(screen)

    if check_collision(player, enemy):
        player.takeDamage(10)
        print("Player collided with enemy")

    pygame.display.update()
    clock.tick(60)
pygame.quit()
