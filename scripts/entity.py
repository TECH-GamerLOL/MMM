import pygame
from config import HEIGHT  # Assuming you have a config file with these constants
from scripts.physic import Physics  # Assuming you have a Physics class for gravity

class Entity:
    def __init__(self, start_x, start_y, size=(50,50), color=(255, 0, 0)):
        if isinstance(size, int):
            size = (size, size)
        
        self.rect = pygame.Rect(start_x, start_y, size[0], size[1])  # Defines the position and size
        self.color = color  # Color of the entity
        self.velocity = 0
        self.isJumping = False
        self.gravity = Physics()  # Assuming you have a Physics class for gravity

    def draw(self, screen):
        """Draw the entity on the screen"""
        pygame.draw.rect(screen, self.color, self.rect)

    def apply_gravity(self):
        """Apply gravity to the entity if needed"""
        self.velocity += self.gravity.gravity  # Assuming gravity is a property of Physics
        self.velocity = min(self.velocity, self.gravity.terminal_velocity)  # Cap the terminal velocity
        self.rect.y += self.velocity
        self.isJumping = self.rect.y < HEIGHT - self.rect.height  # Check if the entity is on the ground
    
    def move(self, direction, speed):
        """Move the entity in a given direction"""
        self.rect.x += direction * speed

    def get_rect(self):
        return self.rect
