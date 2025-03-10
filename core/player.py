import math

class Menkey ():
    def __init__(self, start_x, start_y):
        if not isinstance(start_x,(int, float)) or not isinstance(start_y(int, float)):
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
        
        def move_right(self):
            self.position[0] += self.speed

        def jump(self):
            self.position[1] += self.speed

        