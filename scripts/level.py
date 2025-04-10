class Level:
    def __init__(self, level_number=1):
        self.level_number = level_number

    def start_level(self):
        print(f"Starting level {self.level_number}")

    def complete_level(self):
        print(f"Level {self.level_number} completed")
