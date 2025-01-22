
class Rover():
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def move_forward(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1 
        elif self.direction == 'W':
            self.x -= 1
            
    def move_backward(self):
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1