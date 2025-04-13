import pygame
from scripts.clouds import Clouds
from scripts.player import Menkey
from scripts.enemy import Enemy
from scripts.collision import check_collision
from scripts.obstacle import Platform, MovingPlatform, Spikes, Ground
from config import WIDTH, HEIGHT
from scripts.cam import Camera
from scripts.levels.level1 import Level1
from scripts.levels.finish import Finish
from scripts.enemy import Eagle, GorillaBoss

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menkey Game")
        self.world = pygame.Surface((WIDTH * 3, HEIGHT * 2))  # 3x wide world!
        self.camera = Camera(self.world.get_width(), self.world.get_height())
        self.clock = pygame.time.Clock()
        self.running = True
        self.BLUE = (0, 255, 255)
        self.clouds = Clouds()
        self.sound = None  # Set sound before using it!

        # === Level Loading ===
        self.level = Level1()
        self.obstacles = self.level.obstacles
        self.finish = self.level.finish

        # === Player & Enemy ===
        self.player = Menkey(
            self.level.player_start_x,
            self.level.player_start_y,
            self.level,
            self.sound,
            self.screen
        )
        self.enemy = Enemy(400, 150)


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

        for enemy in self.level.enemies:
            if isinstance(enemy, Eagle):
                enemy.update(self.player)
            else:
                enemy.update(self.obstacles, self.player)

    # Update moving platforms
        for obstacle in self.obstacles:
            if isinstance(obstacle, MovingPlatform):  # Update moving platforms specifically
                obstacle.update()
        
        for enemy in self.level.enemies:
            if check_collision(self.player, enemy):
                self.player.respawn()
                print("Player collided with enemy - respawning")

# Check for collisions between player and spikes
        for obstacle in self.obstacles:
            if isinstance(obstacle, Spikes):
                if self.player.rect.colliderect(obstacle.rect):
                    self.player.respawn()
                    print("Player collided with spikes - respawning")

        if self.finish.check_reached(self.player.rect):
            self.game_finished = True
            print("Level Complete! You reached the finish!")
            self.running = False

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
        
        for obstacle in self.obstacles:
            obstacle.draw(self.world) 

        for enemy in self.level.enemies:
            enemy.draw(self.world)

        self.player.draw(self.world)  # Draw player on the world surface
        self.finish.draw(self.world)
          

# Blit the world surface to the screen with camera offset
        self.finish.draw(self.world)
        self.screen.blit(self.world, (-self.camera.offset.x, -self.camera.offset.y))

        pygame.display.update()


