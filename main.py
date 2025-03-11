import pygame
from core.player import Menkey

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menkey Game")

WHITE = (255, 255, 255)

player = Menkey(100, 300)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    player.draw(screen)

    pygame.display.update() 
    clock.tick(60)  
pygame.quit()
