import random
import pygame

class Cloud:
    def __init__(self, pos, speed, depth):
        self.pos = list(pos)
        self.speed = speed
        self.depth = depth
        self.size = random.randint(60, 120)

    def update(self):
        self.pos[0] += self.speed
        if self.pos[0] > 100000:  
            self.pos[0] = -self.size

    def render(self, surf, offset=(0, 0)):
        render_x = self.pos[0] - offset[0] * self.depth
        render_y = self.pos[1] - offset[1] * self.depth
        x = render_x % (surf.get_width() + self.size) - self.size
        y = render_y % (surf.get_height() + self.size) - self.size

        color = (255, 255, 255)
        for i in range(3):
            ellipse_width = self.size // (2 + i)
            ellipse_height = self.size // (3 + i)
            pygame.draw.ellipse(surf, color, (x + i * (self.size // 3), y, ellipse_width, ellipse_height))

class Clouds:
    def __init__(self, count=16):
        self.clouds = []
        for _ in range(count):
            pos = (random.random() * 99999, random.random() * 99999)
            speed = random.random() * 0.05 + 0.05
            depth = random.random() * 0.6 + 0.2
            self.clouds.append(Cloud(pos, speed, depth))
        self.clouds.sort(key=lambda x: x.depth)

    def update(self):
        for cloud in self.clouds:
            cloud.update()

    def render(self, surf, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surf, offset=offset)
