import pygame

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def get_rect(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        
def check_collision(obj1, obj2):
    return obj1.get_rect().colliderect(obj2.get_rect())

class Game:
    def __init__(self):
        self.player = GameObject(50, 50, 50, 50)
        self.enemy = GameObject(100, 100, 50, 50)
        self.lives = 3
        self.game_over = False

    def update(self):
        if check_collision(self.player, self.enemy):
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
                print("Game Over")
