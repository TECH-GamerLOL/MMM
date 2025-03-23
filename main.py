import pygame
from core.player import Menkey  # Encapsulation: Menkey class encapsulates player attributes and behaviors
from core.enemy import Enemy  # Encapsulation: Enemy class encapsulates enemy attributes and behaviors
from core.collision import check_collision
from core.obstacle import Platform, MovingPlatform, Spikes, Ground  # Inheritance: Platform, MovingPlatform, Spikes, and Ground inherit from Obstacle
from config import WIDTH, HEIGHT

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print("Initialising game")
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menkey Game")

WHITE = (255, 255, 255)

player = Menkey(400, 150)  # Encapsulation: Creating an instance of Menkey class
enemy = Enemy(400, 150)  # Encapsulation: Creating an instance of Enemy class

# Create instances of obstacles, including the ground
obstacles = [
    Ground(0, HEIGHT - 50, WIDTH, 50),  # Inheritance: Ground class inherits from Platform
    Platform(100, 500, 200, 20),  # Inheritance: Platform class inherits from Obstacle
    MovingPlatform(300, 400, 200, 20, 2),  # Inheritance: MovingPlatform class inherits from Obstacle
    Spikes(600, 500, 50, 50)  # Inheritance: Spikes class inherits from Obstacle
]

running = True
clock = pygame.time.Clock()

while running:
    print("Game loop running")
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(obstacles)  # Encapsulation: Updating player state
    player.draw(screen)  # Encapsulation: Drawing player
    player.draw_health(screen)  # Encapsulation: Drawing player's health

    enemy.update(obstacles)  # Encapsulation: Updating enemy state
    enemy.move()  # Encapsulation: Moving enemy
    enemy.draw(screen)  # Encapsulation: Drawing enemy

    # Update and draw obstacles
    for obstacle in obstacles:
        if isinstance(obstacle, MovingPlatform):  # Polymorphism: Checking if obstacle is an instance of MovingPlatform
            obstacle.update()  # Polymorphism: Calling update method on MovingPlatform instance
        obstacle.draw(screen)  # Polymorphism: Calling draw method on obstacle instance

    # Check for collision between player and enemy
    if check_collision(player, enemy):
        player.takeDamage(10)  # Encapsulation: Reducing player's health
        print("Player collided with enemy")

    # Check for collision between player and spikes
    for obstacle in obstacles:
        if isinstance(obstacle, Spikes):  # Polymorphism: Checking if obstacle is an instance of Spikes
            print("Checking spikes collision")
            if player.rect.colliderect(obstacle.rect):
                player.takeDamage(10)  # Encapsulation: Reducing player's health
                print("Player collided with spikes")

    pygame.display.update()
    clock.tick(60)
pygame.quit()
