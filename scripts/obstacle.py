import pygame
from config import HEIGHT, WIDTH

# Base class for obstacles
class Obstacles:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        raise NotImplementedError("This method should be overridden by subclasses")

# Subclass for static platforms
class Platform(Obstacles):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Draw a green platform

# Subclass for moving platforms
class MovingPlatform(Obstacles):
    def __init__(self, x, y, width, height, speed):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left < 0 or self.rect.right > 800:  # Assuming screen width is 800
            self.direction *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)  # Draw a blue moving platform

# Subclass for spikes
class Spikes(Obstacles):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 0, 0), [
            (self.rect.left, self.rect.bottom),
            (self.rect.centerx, self.rect.top),
            (self.rect.right, self.rect.bottom)
        ])  

class Ground(Platform):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (139, 69, 19), self.rect)  