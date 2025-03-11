class Physics:
    def __init__(self, gravity=0.5, terminal_velocity=10):
        self.gravity = gravity
        self.terminal_velocity = terminal_velocity

    def apply_gravity(self, entity):
        entity.velocity += self.gravity  
        entity.velocity = min(entity.velocity, self.terminal_velocity) 
        entity.position[1] += entity.velocity 
