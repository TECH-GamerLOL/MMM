import pygame
from scripts.entity import Entity  
from scripts.physic import Physics
from config import ENEMY_SIZE, ENEMY_SPEED, HEIGHT, WIDTH, CHASE_RANGE

class Enemy(Entity):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, ENEMY_SIZE, (255, 0, 0))  # Call parent class constructor for common properties
        self.rect = pygame.Rect(start_x, start_y, ENEMY_SIZE, ENEMY_SIZE)
        self.gravity = Physics()  # Assuming you have a Physics class for gravity
        self.movement_speed = ENEMY_SPEED
        self.chase_range = CHASE_RANGE  # Range at which the enemy starts chasing the player
        self.velocity = 0  # Initial vertical velocity
        self.alive = True
        self.chaseing = False
    
    def update(self, obstacles, player):  # Accept player as an argument
        if not self.alive:
            return
        """Update the enemy, potentially based on player's position"""
        self.apply_gravity()  # Apply gravity from the Entity class

        distance = abs(self.rect.centerx - player.rect.centerx)
        if distance <= self.chase_range:
            self.chaseing = True
        else:
            self.chaseing = False

        # Only chase if started
        if self.chaseing:
            self.chase(player)

        # Handle collision with obstacles
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if self.velocity > 0:  # If falling
                    self.rect.bottom = obstacle.rect.top
                    self.velocity = 0  # Stop falling

    def chase(self, player):
        """Chase the player if within the chase range"""
        if player.rect.centerx < self.rect.centerx:  # Player is on the left
            self.rect.x -= self.movement_speed
        elif player.rect.centerx > self.rect.centerx:  # Player is on the right
            self.rect.x += self.movement_speed

    def die(self):
        """Handle enemy death"""
        self.alive = False

    def draw(self, screen):
        """Draw the enemy on the screen"""
        super().draw(screen)  # Call parent class draw method

    def get_rect(self):
        return self.rect
