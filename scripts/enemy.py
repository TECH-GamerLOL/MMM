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
        self.direction = 1  # 1 means moving right, -1 means moving left
        self.chase_range = CHASE_RANGE  # Range at which the enemy starts chasing the player
        self.target = None  # Placeholder for player or other target to chase
        self.state = "walk"  # Initial state is walk (you can update this based on behavior)
        self.velocity = 0  # Initialize velocity for gravity handling
    
    def update(self, obstacles, player):  # Accept player as an argument
        """Update the enemy, potentially based on player's position"""
        self.apply_gravity()  # Apply gravity from the Entity class
        self.move()  # Update movement

        # Check if the player is within the chase range
        if abs(self.rect.centerx - player.rect.centerx) <= self.chase_range:
            self.chase(player)  # Start chasing if player is within range

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

    def move(self):
        """Enemy movement behavior"""
        if self.state == "walk":
            self.rect.x += self.direction * self.movement_speed
            if self.rect.x <= 0 or self.rect.x >= WIDTH - ENEMY_SIZE:
                self.direction *= -1  # Reverse direction when hitting screen edges
        elif self.state == "bounce":
            self.rect.x += self.direction * (self.movement_speed * 2)

    def draw(self, screen):
        """Draw the enemy on the screen"""
        super().draw(screen)  # Call parent class draw method

    def get_rect(self):
        return self.rect
