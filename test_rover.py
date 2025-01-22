import pytest

from rover import Rover, Movement, Direction, Map


@pytest.mark.parametrize("x,y,direction,destination_x,destination_y", 
                         [(0, 0, Direction.NORTH, 0, 1),
                          (0, 0, Direction.SOUTH, 0, -1),
                          (0, 0, Direction.EAST, 1, 0),
                          (0, 0, Direction.WEST, -1, 0)]
                        )
def test_move_forward(x,
                      y,
                      direction,
                      destination_x,
                      destination_y
                      ):
    currentMap = Map(11, 11)
    rover = Rover(x, y, direction)
    rover.move_fb(Movement.FORWARD, currentMap)
    
    assert rover.x == destination_x and rover.y == destination_y and rover.direction == direction

@pytest.mark.parametrize("x,y,direction,destination_x,destination_y",
                         [(0, 0, Direction.NORTH, 0, -1),
                          (0, 0, Direction.SOUTH, 0, 1),
                          (0, 0, Direction.EAST, -1, 0),
                          (0, 0, Direction.WEST, 1, 0)]
                         )
def test_move_backward(x,
                       y,
                       direction,
                       destination_x,
                       destination_y
                       ):
    currentMap = Map(11, 11)
    rover = Rover(0,0, direction)
    rover.move_fb(Movement.BACKWARD, currentMap)
    
    assert rover.x == destination_x and rover.y == destination_y and rover.direction == direction

@pytest.mark.parametrize("x,y,init_direction,final_direction",
                         [(0, 0, Direction.NORTH, Direction.WEST),
                          (0, 0, Direction.WEST, Direction.SOUTH),
                          (0, 0, Direction.SOUTH, Direction.EAST),
                          (0, 0, Direction.EAST, Direction.NORTH)]
                         )
def test_turn_left(x, y, init_direction, final_direction):
    rover = Rover(x, y, init_direction)
    rover.turn_lr(Movement.LEFT)

    assert rover.x == x and rover.y == y and rover.direction == final_direction
    
@pytest.mark.parametrize("x,y,init_direction,final_direction",
                            [(0, 0, Direction.NORTH, Direction.EAST),
                             (0, 0, Direction.EAST, Direction.SOUTH),
                             (0, 0, Direction.SOUTH, Direction.WEST),
                             (0, 0, Direction.WEST, Direction.NORTH)]
                            )
def test_turn_right(x, y, init_direction, final_direction):
    rover = Rover(x, y, init_direction)
    rover.turn_lr(Movement.RIGHT)

    assert rover.x == x and rover.y == y and rover.direction == final_direction
    
def test_bulk_move():
    currentMap = Map(11, 11)
    movements = [Movement.FORWARD, Movement.LEFT, Movement.FORWARD, Movement.LEFT, Movement.BACKWARD, Movement.RIGHT]
    rover = Rover(0, 0, Direction.NORTH)
    rover.bulk_move(movements, currentMap)
    
    assert rover.x == -1 and rover.y == 2 and rover.direction == Direction.WEST
    
def test_wrapping_edges():
    currentMap = Map(11, 11)
    rover = Rover(0, 0, Direction.NORTH)
    
    for _ in range(8):
        rover.move_fb(Movement.FORWARD, currentMap)
    
    assert rover.x == 0 and rover.y == -3 and rover.direction == Direction.NORTH