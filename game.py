import pygame
from scripts.clouds import Clouds
from scripts.player import Menkey
from scripts.enemy import Enemy
from scripts.collision import check_collision
from scripts.obstacle import Platform, MovingPlatform, Spikes, Ground
from config import WIDTH, HEIGHT
from scripts.level import Level
from scripts.cam import Camera

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menkey Game")
        self.world = pygame.Surface((WIDTH * 2, HEIGHT * 2))  # Create a surface that's twice as big as the screen
        self.camera = Camera(WIDTH, HEIGHT)
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_finished = False
        self.world = pygame.Surface((WIDTH * 3, HEIGHT * 2))  # 3x wide world!
        self.camera = Camera(self.world.get_width(), self.world.get_height())
        self.BLUE = (0, 255, 255)
        self.clouds = Clouds()
        self.level = Level()
        self.sound = None  # Set to None initially or load your sound files

        # Initialize the player and enemy
        self.player = Menkey(400, 150, self.level, self.sound, self.screen)
        self.enemy = Enemy(400, 150)

        # Create obstacles (Ground, Platform, Spikes, etc.)
        self.obstacles = [
            Ground(0, HEIGHT - 50, 3000, 50),
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
    def update_camera(self):
        if self.player.rect.centerx > WIDTH // 2 and self.player.rect.centerx < self.level.width - WIDTH // 2:
            self.camera_x = self.player.rect.centerx - WIDTH // 2
        elif self.player.rect.centerx <= WIDTH // 2:
            self.camera_x = 0
        else:
            self.camera_x = self.level.width - WIDTH

        self.camera.offset.x = self.camera_x

    def render(self):
        self.clouds.render(self.screen)
        self.world.fill(self.BLUE)  # Fill world with background color first

        self.camera.update(self.player.rect)  # Update camera position based on the player
# Draw enemy and player after obstacles
        pygame.draw.rect(self.world, (255, 0, 0), self.enemy.rect)     # Enemy
        pygame.draw.rect(self.world, (255, 200, 69), self.player.rect)  # Player

# Draw obstacles on the world surface
        for obstacle in self.obstacles:
            pygame.draw.rect(self.world, (100, 100, 100), obstacle.rect)  # Obstacles


# Blit the world surface to the screen with camera offset
        self.screen.blit(self.world, (-self.camera.offset.x, -self.camera.offset.y))

        pygame.display.update()


