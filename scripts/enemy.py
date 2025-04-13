import pygame
from scripts.entity import Entity  
from scripts.physic import Physics
from config import ENEMY_SIZE, ENEMY_SPEED, CHASE_RANGE

class Enemy(Entity):
    def __init__(self, start_x, start_y, color=(255, 0, 0)):  # <-- Add color here
        super().__init__(start_x, start_y, ENEMY_SIZE, color)  # <-- Pass to Entity
        self.gravity = Physics()
        self.movement_speed = ENEMY_SPEED
        self.chase_range = CHASE_RANGE
        self.velocity = 0
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
class Snake(Enemy):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, color = (255, 255, 0))
        self.movement_speed = 2  # Slower, ground-based
        self.chase_range = 150   # Short detection

class GorillaBoss(Enemy):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, color = (150, 75, 100))
        self.movement_speed = 1   # Slow but powerful
        self.chase_range = 500    # Big boss awareness
        self.health = 100

    def chase(self, player):
        if self.health < 50:
            self.movement_speed = 3  # Enrage when low HP
        super().chase(player)


class Eagle(Enemy):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y, color = (0, 100, 255))
        self.movement_speed = 4         # Faster chase speed
        self.chase_range = 300          # Large detection
        self.hover_y = start_y          # Fixed flying height

    def apply_gravity(self):
        # Override gravity: eagle stays in the air at hover_y
        self.rect.y = self.hover_y

    def update(self, player):
        if not self.alive:
            return
        self.apply_gravity()  # Lock vertical position
        distance = abs(self.rect.centerx - player.rect.centerx)
        self.chasing = distance <= self.chase_range
        if self.chasing:
            self.chase(player)  # Move horizontally toward player

