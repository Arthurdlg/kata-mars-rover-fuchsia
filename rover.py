from enum import Enum

class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3
    
class Movement(Enum):
    F = 1
    B = -1
    L = 0
    R = 2

class Rover():
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        
    def move_fb(self, movement):
        if self.direction == Direction.N:
            self.y += movement.value
        elif self.direction == Direction.S:
            self.y -= movement.value
        elif self.direction == Direction.E:
            self.x += movement.value
        elif self.direction == Direction.W:
            self.x -= movement.value
            
    def turn_lr(self, movement):
        self.direction = Direction((self.direction.value + movement.value - 1) % 4)
        
    def bulk_move(self, movements):
        for movement in movements:
            print(movement)
            if movement in [Movement.F, Movement.B]:
                self.move_fb(movement)
                print(self.x, self.y, self.direction)
            else:
                self.turn_lr(movement)
                print(self.x, self.y, self.direction)