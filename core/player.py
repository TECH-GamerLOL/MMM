import math
import pygame
from core.physic import Physics
from core.entity import Entity

import sys
print(sys.path)  
print("Physics module loaded:", 'core.physic' in sys.modules)


class Menkey (Entity):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, 40, (0, 0, 255))
        self.rect = pygame.Rect(start_x, start_y, 40, 40)
        self.color = (0, 0, 255)
        self.gravity = Physics()  # Initialize gravity as an instance of the Physics class
        self.position = [start_x, start_y]
        self.velocity = 0
        self.isJumping = False
        self.groundY = start_y
        self.health = 3
        self.speed = 2
        self.power = []
        self.invincible = False
    
    def moveLeft(self):
        self.position[0] -= self.speed
        
    def moveRight(self):
        self.position[0] += self.speed

    def jump(self):
        if not self.isJumping:  
            self.velocity = -10  
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
            return
    
    def draw(self, screen):
        self.color = [200, 200, 200]
        self.size = 20
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))  # Draw player

    def update(self):
        self.gravity.apply_gravity(self)  # Apply gravity to player

        if self.rect.y >= self.groundY:  # Check if player has reached the ground
            self.rect.y = self.groundY  # Make sure player stays on the ground
            self.velocity = 0  # Reset velocity when on the ground
            self.gravity = 2.0  # Temporarily increase gravity to test
            self.groundY = 400  # Example ground level
            self.isJumping = False  # No longer jumping when on the ground
    
        self.handle_input()  # Handle player input (e.g., left, right, jump)

        print(f"Player position: {self.rect.y}, Velocity: {self.velocity}")



