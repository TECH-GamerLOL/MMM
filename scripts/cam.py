import pygame
from config import HEIGHT, WIDTH  

class Camera:
    def __init__(self, width, height):
        self.offset = pygame.Vector2(0, 0)
        self.width = width
        self.height = height

    def update(self, target_rect):
        self.offset.x = target_rect.centerx - WIDTH // 2
        self.offset.y = target_rect.centery - HEIGHT // 2

        self.offset.x = max(0, min(self.offset.x, self.width - WIDTH))
        self.offset.y = max(0, min(self.offset.y, self.height - HEIGHT))

    def apply(self, rect):
        # Return a new rect with the camera offset applied
        return rect.move(-self.offset.x, -self.offset.y)

