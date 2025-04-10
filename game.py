import pygame
from scripts.clouds import Clouds  # Encapsulation: Clouds class encapsulates cloud attributes and behaviors
from scripts.player import Menkey  # Encapsulation: Menkey class encapsulates player attributes and behaviors
from scripts.enemy import Enemy  # Encapsulation: Enemy class encapsulates enemy attributes and behaviors
from scripts.collision import check_collision
from scripts.obstacle import Platform, MovingPlatform, Spikes, Ground  # Inheritance: Platform, MovingPlatform, Spikes, and Ground inherit from Obstacle
from config import WIDTH, HEIGHT

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menkey Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.BLUE = (0, 255, 255)

        self.clouds = Clouds()

        self.player = Menkey(400, 150)  # Encapsulation: Creating an instance of Menkey class
        self.enemy = Enemy(400, 150)  # Encapsulation: Creating an instance of Enemy class

        # Create instances of obstacles, including the ground
        self.obstacles = [
            Ground(0, HEIGHT - 50, WIDTH, 50),  # Inheritance: Ground class inherits from Platform
            Platform(100, 500, 200, 20),  # Inheritance: Platform class inherits from Obstacle
            MovingPlatform(300, 400, 200, 20, 2),  # Inheritance: MovingPlatform class inherits from Obstacle
            Spikes(600, 500, 50, 50)  # Inheritance: Spikes class inherits from Obstacle
        ]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.clouds.update()  # Encapsulation: Updating clouds

        self.player.update(self.obstacles)  # Encapsulation: Updating player state
        self.enemy.update(self.obstacles)  # Encapsulation: Updating enemy state
        self.enemy.move()  # Encapsulation: Moving enemy

        # Update moving platforms
        for obstacle in self.obstacles:
            if isinstance(obstacle, MovingPlatform):  # Polymorphism: Checking if obstacle is an instance of MovingPlatform
                obstacle.update()  # Polymorphism: Calling update method on MovingPlatform instance

        # Check for collision between player and enemy
        if check_collision(self.player, self.enemy):
            self.player.takeDamage(10)  # Encapsulation: Reducing player's health
            print("Player collided with enemy")

        # Check for collision between player and spikes
        for obstacle in self.obstacles:
            if isinstance(obstacle, Spikes):  # Polymorphism: Checking if obstacle is an instance of Spikes
                if self.player.rect.colliderect(obstacle.rect):
                    self.player.takeDamage(10)  # Encapsulation: Reducing player's health
                    print("Player collided with spikes")

    def render(self):
        self.screen.fill(self.BLUE)

        self.clouds.render(self.screen)  # Encapsulation: Rendering clouds

        self.player.draw(self.screen)  # Encapsulation: Drawing player
        self.player.draw_health(self.screen)  # Encapsulation: Drawing player's health

        self.enemy.draw(self.screen)  # Encapsulation: Drawing enemy

        # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)  # Polymorphism: Calling draw method on obstacle instance

        pygame.display.update()