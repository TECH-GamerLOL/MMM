import pygame

class Finish:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 100)  # Example flag size

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 215, 0), self.rect)  # Gold flag

    def check_reached(self, player_rect):
        return self.rect.colliderect(player_rect)
