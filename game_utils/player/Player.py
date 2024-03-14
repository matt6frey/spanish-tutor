class Player():
    name = ''
    points = 0
    
    def __init__(self, name):
        self.name = name
    
    def get_points(self):
        return self.points
    
    def add_point(self):
        self.points += 1
    