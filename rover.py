
class Rover():
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def move_forward(self):
        if self.direction == 'N':
            self.y += 1