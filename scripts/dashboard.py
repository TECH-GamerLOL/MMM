import pygame

class Dashboard:
    def __init__(self):
        # Initialize dashboard components, like health or score
        self.font = pygame.font.Font(None, 36)  # Default font, you can replace with a specific one
        self.health = 100  # Initialize health to 100

    def draw(self, screen):
        # Render the health (or other stats) on the screen
        health_text = self.font.render(f'Health: {self.health}', True, (255, 0, 0))  # Red color for health
        screen.blit(health_text, (10, 10))  # Draw health at the top left

    def update_health(self, health):
        # Update the health displayed on the dashboard
        self.health = health
