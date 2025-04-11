import pygame
from scripts.clouds import Clouds
from scripts.player import Menkey
from scripts.enemy import Enemy
from scripts.collision import check_collision
from scripts.obstacle import Platform, MovingPlatform, Spikes, Ground
from config import WIDTH, HEIGHT
from scripts.level import Level

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menkey Game")

        self.clock = pygame.time.Clock()
        self.running = True
        self.BLUE = (0, 255, 255)
        self.clouds = Clouds()
        self.level = Level()
        self.sound = None  # Set to None initially or load your sound files

        # Initialize the player and enemy
        self.player = Menkey(400, 150, self.level, self.sound, self.screen)
        self.enemy = Enemy(400, 150)

        # Create obstacles (Ground, Platform, Spikes, etc.)
        self.obstacles = [
            Ground(0, HEIGHT - 50, WIDTH, 50),
            Platform(100, 500, 200, 20),
            MovingPlatform(300, 400, 200, 20, 2),  # Moving platform with speed of 2
            Spikes(600, 500, 50, 50)
        ]

    def run(self): 
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Run the game at 60 FPS
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.clouds.update()  # Update cloud movement

        self.player.update(self.obstacles)  # Update player state
        self.enemy.update(self.obstacles, self.player)  # Pass player to the enemy's update method
        self.enemy.move()  # Move the enemy

    # Update moving platforms
        for obstacle in self.obstacles:
            if isinstance(obstacle, MovingPlatform):  # Update moving platforms specifically
                obstacle.update()

    # Check for collisions between player and enemy
        if check_collision(self.player, self.enemy):
            self.player.respawn()
            print("Player collided with enemy - respawning")

# Check for collisions between player and spikes
        for obstacle in self.obstacles:
            if isinstance(obstacle, Spikes):
                if self.player.rect.colliderect(obstacle.rect):
                    self.player.respawn()
                    print("Player collided with spikes - respawning")

    def render(self):
        self.screen.fill(self.BLUE)  # Fill screen with blue background

        self.clouds.render(self.screen)  # Render the clouds
        self.player.draw(self.screen)  # Draw the player

    # Call the Dashboard's draw method to display the health and other stats
        #self.dashboard.draw(self.screen)

        self.enemy.draw(self.screen)  # Draw the enemy

    # Draw obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

    # Draw the dashboard (health, score, etc.)
        pygame.display.update()  # Update the screen display

