import math
import pygame

class Menkey ():
    def __init__(self, start_x, start_y):
        if not isinstance(start_x, (int, float)) or not isinstance(start_y, (int, float)):
            print("Must be num")
            return
        if start_x < 0 or start_y < 0:
            print("Can't be negative")
            return
        
        self.position = [start_y, start_x]
        self.health = 3
        self.speed = 2
        self.power = []
        self.invincible = False
    
    def moveLeft(self):
        self.position[0] -= self.speed
        
    def moveRight(self):
        self.position[0] += self.speed

    def jump(self):
        self.position[1] += self.speed
            
    def handle_input(self):  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_SPACE]:
            self.jump()

    def takeDamage(damage, self):
        if not self.invincible:
            if damage < 0:
                print("Damage mus be positive")
                return
            return
                