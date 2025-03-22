class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_rect(self):
        return (self.x, self.y, self.width, self.height)

def check_collision(obj1, obj2):
    rect1 = obj1.get_rect()
    rect2 = obj2.get_rect()

    if (rect1[0] < rect2[0] + rect2[2] and
        rect1[0] + rect1[2] > rect2[0] and
        rect1[1] < rect2[1] + rect2[3] and
        rect1[1] + rect1[3] > rect2[1]):
        return True
    return False

class Game:
    def __init__(self):
        self.player = GameObject(50, 50, 50, 50)
        self.enemy = GameObject(100, 100, 50, 50)
        self.lives = 3
        self.game_over = False

    def update(self):
        if check_collision(self.player, self.enemy):
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
                print("Game Over")
