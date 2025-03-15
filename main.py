import pygame
from core.player import Menkey
from core.enemy import Enemy
from config import WIDTH, HEIGHT

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menkey Game")

WHITE = (255, 255, 255)

player = Menkey(400, 300)
enemy = Enemy(400,150)  

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    player.update()
    print(f"Velocity:, Position:")
    player.draw(screen)
    enemy.update()
    enemy.move()  
    enemy.draw(screen)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
