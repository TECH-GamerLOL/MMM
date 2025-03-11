import math
import pygame
from core.physic import Physics

import sys
print(sys.path)  
print("Physics module loaded:", 'core.physic' in sys.modules)


class Menkey ():
    def __init__(self, start_x, start_y):
        if not isinstance(start_x, (int, float)) or not isinstance(start_y, (int, float)):
            print("Must be num")
            return
        if start_x < 0 or start_y < 0:
            print("Can't be negative")
            return
        self.position = [start_x, start_y]
        self.velocity = 0
        self.gravity = Physics()
        self.isJumping = False
        self.groundY = start_y

        self.position = [start_y, start_x]
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
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))  # Draw player
        pygame.draw.rect(screen, (100, 50, 0), (0, self.groundY + self.size, 800, 20))

    def update(self):
        self.gravity.apply_gravity(self)  
        if self.position[1] >= self.groundY:
            self.position[1] = self.groundY
            self.velocity = 0
            self.isJumping = False
