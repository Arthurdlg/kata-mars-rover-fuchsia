from enum import Enum

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3
    
class Movement(Enum):
    FORWARD = 1
    BACKWARD = -1
    LEFT = 0
    RIGHT = 2
    
class Map():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rover():
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move_fb(self, movement, currentMap):
        half_width = currentMap.width // 2
        half_height = currentMap.height // 2

        if self.direction == Direction.NORTH:
            self.y = (self.y + movement.value + half_height) % currentMap.height - half_height
        elif self.direction == Direction.SOUTH:
            self.y = (self.y - movement.value + half_height) % currentMap.height - half_height
        elif self.direction == Direction.EAST:
            self.x = (self.x + movement.value + half_width) % currentMap.width - half_width
        elif self.direction == Direction.WEST:
            self.x = (self.x - movement.value + half_width) % currentMap.width - half_width
            
    def turn_lr(self, movement):
        self.direction = Direction((self.direction.value + movement.value - 1) % 4)
        
    def bulk_move(self, movements, currentMap):
        for movement in movements:
            print(movement)
            if movement in [Movement.FORWARD, Movement.BACKWARD]:
                self.move_fb(movement, currentMap)
                print(self.x, self.y, self.direction)
            else:
                self.turn_lr(movement)
                print(self.x, self.y, self.direction)