import pygame
from scripts.entity import Entity  # Inherit from the Entity class
from config import HEIGHT, PLAYER_SIZE, PLAYER_SPEED, PLAYER_JUMP

class Menkey(Entity):
    def __init__(self, x, y, level, sound, screen):
        super().__init__(x, y, PLAYER_SIZE, (0, 255, 0))  # Call parent class constructor for common properties
        self.level = level
        self.sound = sound
        self.screen = screen
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

    def respawn(self):
        self.position = [100, HEIGHT - PLAYER_SIZE]  # or your desired start position
        self.velocity = 0
        self.isJumping = False
        self.rect.topleft = self.position
        print("Player respawned.")

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
            self.respawn()
            return


        if on_ground:
            self.isJumping = False

        self.rect.x = self.position[0]

    def draw(self, screen):
        """Draw the player on the screen"""
        super().draw(screen)  # Call parent class draw method
