import pygame
from scripts.physic import Physics
from scripts.entity import Entity  # Inherit from the Entity class
from config import HEIGHT, PLAYER_SIZE, PLAYER_HEALTH, PLAYER_SPEED, PLAYER_GROUND_TOLERANCE, PLAYER_JUMP

class Menkey(Entity):
    def __init__(self, x, y, dashboard, level, sound, screen):
        super().__init__(x, y, PLAYER_SIZE, (0, 255, 0))  # Call parent class constructor for common properties
        self.dashboard = dashboard
        self.level = level
        self.sound = sound
        self.screen = screen
        self.health = PLAYER_HEALTH
        self.invincible = False
        self.invincible_time = 0
        self.isJumping = False
        self.speed = PLAYER_SPEED
        self.position = [x, y]
        self.velocity = 0

    def handle_input(self):  
        """Handle input for movement"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.moveRight()
        if keys[pygame.K_SPACE]:
            self.jump()

    def moveLeft(self):
        self.position[0] -= self.speed
        
    def moveRight(self):
        self.position[0] += self.speed

    def jump(self):
        if not self.isJumping:  
            self.velocity = -PLAYER_JUMP
            self.isJumping = True
            print(f"Jump triggered! Velocity: {self.velocity}")

    def takeDamage(self, damage):
        if not self.invincible:
            self.health -= damage
            self.health = max(0, self.health)  # Ensure health doesn't go below 0
            self.invincible = True
            self.invincible_time = pygame.time.get_ticks()  # Record the time the player took damage
            print(f"Player took {damage} damage. Health: {self.health}")
        
        if self.health <= 0:
            print("Player is dead")
        
        # Update the dashboard with the new health value
        self.dashboard.update_health(self.health)

    def update(self, obstacles):
        """Update player status and handle collisions"""
        self.handle_input()
        self.apply_gravity()  # Apply gravity from the Entity class

        on_ground = False 
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if self.velocity > 0:  # Falling down
                    self.rect.bottom = obstacle.rect.top  
                    self.position[1] = self.rect.y  
                    self.velocity = 0
                    on_ground = True
                elif self.velocity < 0:  # Hitting the ceiling
                    self.rect.top = obstacle.rect.bottom  
                    self.position[1] = self.rect.y
                    self.velocity = 0

        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.position[1] = self.rect.y
            self.velocity = 0
            on_ground = True

        if on_ground:
            self.isJumping = False

        self.rect.x = self.position[0]

    def draw(self, screen):
        """Draw the player on the screen"""
        super().draw(screen)  # Call parent class draw method

        # Draw player health or other UI elements here if needed
        self.dashboard.draw(screen)
