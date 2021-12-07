from fish import Fish

class FishTracker:
    def __init__(self, initial_fish):
        self.fishies = [
            Fish(timer)
            for timer in initial_fish
        ]
        self.days_past = 0
    
    def pass_day(self):
        self.spawn_fishies()
        for fish in self.fishies:
            fish.age()
        self.days_past += 1
    
    def spawn_fishies(self):
        new_fishies = []
        for fish in self.fishies:
            if fish.timer == 0:
                new_fishies.append(Fish(9))
                fish.reset()
        self.fishies.extend(new_fishies)
    
    def __str__(self):
        report = ""
        if self.days_past == 0:
            label = "Initial state: "
        elif self.days_past == 1:
            label = "After 1  day:  "
        else:
            label = f"After {str(self.days_past):2} days: "
        report += label
        report += ",".join(str(fish.timer) for fish in self.fishies)
        return report