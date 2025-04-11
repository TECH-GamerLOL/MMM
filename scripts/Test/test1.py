import pygame
from scripts.physic import Physics
from scripts.entity import Entity
from config import HEIGHT, PLAYER_SIZE, PLAYER_HEALTH, PLAYER_SPEED, PLAYER_GROUND_TOLERANCE, PLAYER_JUMP

class Menkey(Entity):
    def __init__(self, start_x, start_y, level, dashboard, sound, screen):
        super().__init__(start_x, start_y, 40, (10, 0, 0))
        self.rect = pygame.Rect(start_x, start_y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = (0, 0, 255)
        self.gravity = Physics()
        self.position = [start_x, start_y]
        self.velocity = 0
        self.isJumping = False
        self.groundY = HEIGHT - PLAYER_SIZE
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.power = []
        self.invincible = False
        self.invincible_time = 0
        self.invincible_duration = 1000  # milliseconds
        self.ground_tolerence = PLAYER_GROUND_TOLERANCE

        self.dashboard = dashboard
        self.level = level
        self.sound = sound
        self.screen = screen

    def handle_input(self):
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

    def bounce(self):
        self.velocity = -PLAYER_JUMP // 1.5  # Bounce with less power

    def takeDamage(self, damage):
        if not self.invincible:
            self.health -= damage
            self.health = max(0, self.health)
            self.invincible = True
            self.invincible_time = pygame.time.get_ticks()
            print(f"Player took {damage} damage. Health: {self.health}")
            if self.health <= 0:
                print("Player is dead")

    def update(self, obstacles):
        self.handle_input()

        # Invincibility timer logic
        if self.invincible and (pygame.time.get_ticks() - self.invincible_time > self.invincible_duration):
            self.invincible = False

        self.velocity += self.gravity.gravity
        self.velocity = min(self.velocity, self.gravity.terminal_velocity)

        self.position[1] += self.velocity
        self.rect.y = self.position[1]

        on_ground = False
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if self.velocity > 0:
                    self.rect.bottom = obstacle.rect.top
                    self.position[1] = self.rect.y
                    self.velocity = 0
                    on_ground = True
                elif self.velocity < 0:
                    self.rect.top = obstacle.rect.bottom
                    self.position[1] = self.rect.y
                    self.velocity = 0

        if self.rect.bottom >= self.groundY:
            self.rect.bottom = self.groundY
            self.position[1] = self.rect.y
            self.velocity = 0
            on_ground = True

        if on_ground:
            self.isJumping = False

        self.rect.x = self.position[0]

        # Simplified entity collision logic
        self.check_entity_collisions()

    def check_entity_collisions(self):
        for ent in self.level.entityList:
            if self.rect.colliderect(ent.rect):
                if hasattr(ent, "type") and ent.type == "Item":
                    self.collect_item(ent)
                elif hasattr(ent, "type") and ent.type == "Mob":
                    self.handle_mob_collision(ent)

    def collect_item(self, item):
        self.level.entityList.remove(item)
        self.dashboard.points += 100
        self.dashboard.coins += 1
        self.sound.play_sfx(self.sound.coin)

    def handle_mob_collision(self, mob):
        if not self.invincible:
            self.takeDamage(1)
            self.sound.play_sfx(self.sound.pipe)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], PLAYER_SIZE, PLAYER_SIZE))

    def draw_health(self, screen):
        for i in range(self.health):
            pygame.draw.rect(screen, (255, 0, 0), (20 + i * 15, 20, 12, 12))
