class Octopus:
    def __init__(self, location, value, neighbors):
        self.location = location
        self.value = int(value)
        self.neighbors = neighbors
    
    def increase_value(self):
        self.value += 1

    def reset_value(self):
        self.value = 0

    def flash(self):
        if self.value > 9:
            self.value = 0
            return True
        return False
    
    def __str__(self):
        octopus_string = f"""
        Octopus at {self.location} 
        has value {self.value}
        and neigbors {self.neighbors}
        """
        return octopus_string