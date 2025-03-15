import math
import pygame
from core.physic import Physics
from core.entity import Entity
from config import HEIGHT, PLAYER_SIZE, PLAYER_HEALTH, PLAYER_SPEED, PLAYER_GROUND_TOLERANCE, PLAYER_JUMP

import sys
print(sys.path)  
print("Physics module loaded:", 'core.physic' in sys.modules)


class Menkey (Entity):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, 40, (0, 0, 0))
        self.rect = pygame.Rect(start_x, start_y, 40, 40)
        self.color = (0, 0, 255)
        self.gravity = Physics()  # Initialize gravity as an instance of the Physics class
        self.position = [start_x, start_y]
        self.velocity = 0
        self.isJumping = False
        self.groundY = HEIGHT - PLAYER_SIZE
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.power = []
        self.invincible = False
        self.ground_tolerence = PLAYER_GROUND_TOLERANCE
    
    def moveLeft(self):
        self.position[0] -= self.speed
        
    def moveRight(self):
        self.position[0] += self.speed

    def jump(self):
        if not self.isJumping:  
            self.velocity = -PLAYER_JUMP
            self.isJumping = True


    def handle_input(self):  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.moveRight()
        if keys[pygame.K_SPACE]:
            self.jump()

    def takeDamage(damage, self):
        if not self.invincible:
            if damage < 0:
                print("Damage mus be positive")
                return
            self.health -= damage
    
    def draw(self, screen):
        self.color = [200, 200, 200]
        self.size = PLAYER_SIZE
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))  # Draw player

    def update(self):
        self.handle_input()

        self.gravity.apply_gravity(self)  
        self.position[1] += self.velocity
        self.rect.y = self.position[1]

        if self.rect.y >= self.groundY - self.ground_tolerence:  # Check if player has reached the ground
            self.rect.y = self.groundY  # Make sure player stays on the ground
            self.velocity = 0  # Reset velocity when on the ground
            self.isJumping = False  # No longer jumping when on the ground

        print(f"Player position: {self.rect.y}, Velocity: {self.velocity}")



