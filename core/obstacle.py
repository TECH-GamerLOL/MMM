import pygame

# Base class for obstacles
class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        raise NotImplementedError("This method should be overridden by subclasses")

# Subclass for static platforms
class Platform(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)  # Draw a green platform

# Subclass for moving platforms
class MovingPlatform(Obstacle):
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
class Spikes(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 0, 0), [
            (self.rect.left, self.rect.bottom),
            (self.rect.centerx, self.rect.top),
            (self.rect.right, self.rect.bottom)
        ])  # Draw red spikes

# Example usage in main.py
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    obstacles = [
        Platform(100, 500, 200, 20),
        MovingPlatform(300, 400, 200, 20, 2),
        Spikes(600, 500, 50, 50)
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear screen with black

        for obstacle in obstacles:
            if isinstance(obstacle, MovingPlatform):
                obstacle.update()
            obstacle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()