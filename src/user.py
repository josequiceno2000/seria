
class User:
    high_scores = []

    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def record_run(self):
        User.high_scores.append([self.name, self.score])
    
    def increase_score(self):
        self.score += 1