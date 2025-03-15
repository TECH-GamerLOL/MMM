class Physics:
    def __init__(self, gravity=0.5, terminal_velocity=10):
        self.gravity = gravity
        self.terminal_velocity = terminal_velocity

    def apply_gravity(self, entity):
        if entity.isJumping:
            entity.velocity += self.gravity
            entity.velocity = min(entity.velocity, self.terminal_velocity)
        else:
            entity.velocity = 0
    
        if entity.rect.y < entity.groundY:  # Apply gravity if the player is not on the ground
            entity.velocity += self.gravity  # Increase velocity due to gravity
            entity.velocity = min(entity.velocity, self.terminal_velocity)  # Cap velocity at terminal velocity
        else:
            entity.velocity = 0  # Stop downward movement once on the ground
            entity.rect.y = entity.groundY  # Ensure player stays at the ground level

        entity.rect.y += entity.velocity  # Update the player's position with velocity
