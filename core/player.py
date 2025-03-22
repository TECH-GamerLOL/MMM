import pygame
from core.physic import Physics
from core.entity import Entity
from core.collision import check_collision
from config import HEIGHT, PLAYER_SIZE, PLAYER_HEALTH, PLAYER_SPEED, PLAYER_GROUND_TOLERANCE, PLAYER_JUMP

import sys
print(sys.path)  
print("Physics module loaded:", 'core.physic' in sys.modules)


class Menkey (Entity):
    def get_rect(self):
        return self.rect
    
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, 40, (10, 0, 0))
        self.rect = pygame.Rect(start_x, start_y, PLAYER_SIZE, PLAYER_SIZE)
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
        self.invincible_time = 0
        self.ground_tolerence = PLAYER_GROUND_TOLERANCE
    
    def moveLeft(self):
        self.position[0] -= self.speed
        
    def moveRight(self):
        self.position[0] += self.speed

    def jump(self):
        if not self.isJumping:  
            self.velocity = -PLAYER_JUMP
            self.isJumping = True
            print(f"Jump triggered! Velocity: {self.velocity}")


    def handle_input(self):  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.moveRight()
        if keys[pygame.K_SPACE]:
            print("Jumping")
            self.jump()

    def takeDamage(self, damage):
        if not self.invincible:
            if damage < 0:
                print("Damage must be positive")
                return
            self.health -= damage
            self.health = max(0, self.health)
            self.invincible = True
            self.invincible_time = pygame.time.get_ticks()
            print(f"Player took {damage} damage. Health: {self.health}")

        if self.health <= 0:
            print("Player is dead")
    
    def draw(self, screen):
        self.color = [200, 200, 200]
        self.size = PLAYER_SIZE
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))  # Draw player

    def draw_health(self, screen):
        print(f"Drawing health: {self.health}")  
        if self.health <= 0:
            print("No health left!")
        return  

        for i in range(self.health):
            pygame.draw.rect(screen, (255, 0, 0), (20 + i * 15, 20, 12, 12))  


    def update(self):
        self.handle_input()

        print(f"Before gravity: Position: {self.rect.y}, Velocity: {self.velocity}")

        self.gravity.apply_gravity(self)  
        self.position[1] += self.velocity
        self.rect.y = self.position[1]

        if self.isJumping:
            self.velocity += self.gravity.gravity
        
        print(f"After gravity: Position: {self.rect.y}, Velocity: {self.velocity}")

        if self.rect.y >= self.groundY - self.ground_tolerence:  # Check if player has reached the ground
            self.rect.y = self.groundY  # Make sure player stays on the ground
            self.velocity = 0  # Reset velocity when on the ground
            self.isJumping = False  # No longer jumping when on the ground
        
        if self.invincible:
            if pygame.time.get_ticks() - self.invincible_time > 2000:
                self.invincible = False
                print("Player is not invincible")

        print(f"Player position: {self.rect.y}, Velocity: {self.velocity}")



