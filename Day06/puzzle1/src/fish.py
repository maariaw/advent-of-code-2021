class Fish:
    def __init__(self, timer):
        self.timer = timer
    
    def age(self):
        self.timer -= 1
    
    def reset(self):
        self.timer = 7