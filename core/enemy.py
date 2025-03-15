import pygame
from core.entity import Entity  
from core.physic import Physics
from config import ENEMY_SIZE, ENEMY_SPEED, WIDTH, HEIGHT

class Enemy(Entity):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, ENEMY_SIZE, (255, 0, 0))  # Red color
        self.rect = pygame.Rect(start_x, start_y, ENEMY_SIZE, ENEMY_SIZE)
        self.gravity = Physics()  # Create a physics object for gravity
        self.groundY = HEIGHT - ENEMY_SIZE
        self.velocity = 0
        self.direction = 1  # 1 means moving right, -1 means moving left
        self.movement_speed = ENEMY_SPEED
        self.isJumping = False
        print(f"Enemy created at ({start_x}, {start_y})")

    def move(self):
        self.rect.x += self.direction * self.movement_speed
        if self.rect.x <= 0 or self.rect.x >= WIDTH - ENEMY_SIZE:
            self.direction *= -1  # Reverse direction when hitting the boundaries

    def update(self):
        self.gravity.apply_gravity(self)  # Apply gravity to enemy
        if self.rect.y == self.groundY:  # Enemy is on the ground, stop falling
            self.isJumping = False
        self.move()  # Move the enemy based on the AI logic (e.g., direction, speed)

