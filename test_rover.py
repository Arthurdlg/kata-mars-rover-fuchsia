import pytest

from rover import Rover, Movement, Direction


@pytest.mark.parametrize("x,y,direction,destination_x,destination_y", 
                         [(0,0,Direction.N,0,1),
                          (0,0,Direction.S,0,-1),
                          (0,0,Direction.E,1,0),
                          (0,0,Direction.W,-1,0)]
                        )
def test_move_forward(x,
                      y,
                      direction,
                      destination_x,
                      destination_y
                      ):
    rover = Rover(0, 0, direction)
    rover.move_fb(Movement.F)
    
    assert rover.x == destination_x and rover.y == destination_y and rover.direction == direction

@pytest.mark.parametrize("x,y,direction,destination_x,destination_y",
                         [(0,0,Direction.N,0,-1),
                          (0,0,Direction.S,0,1),
                          (0,0,Direction.E,-1,0),
                          (0,0,Direction.W,1,0)]
                         )
def test_move_backward(x,
                       y,
                       direction,
                       destination_x,
                       destination_y
                       ):
    rover = Rover(0,0, direction)
    rover.move_fb(Movement.B)
    
    assert rover.x == destination_x and rover.y == destination_y and rover.direction == direction

@pytest.mark.parametrize("x,y,init_direction,final_direction",
                         [(0,0,Direction.N, Direction.W),
                        (0,0,Direction.W, Direction.S),
                        (0,0,Direction.S, Direction.E),
                        (0,0,Direction.E, Direction.N)]
                         )
def test_turn_left(x, y, init_direction, final_direction):
    rover = Rover(x, y, init_direction)
    rover.turn_lr(Movement.L)

    assert rover.x == x and rover.y == y and rover.direction == final_direction
    
@pytest.mark.parametrize("x,y,init_direction,final_direction",
                            [(0,0,Direction.N, Direction.E),
                            (0,0,Direction.E, Direction.S),
                            (0,0,Direction.S, Direction.W),
                            (0,0,Direction.W, Direction.N)]
                            )
def test_turn_right(x, y, init_direction, final_direction):
    rover = Rover(x, y, init_direction)
    rover.turn_lr(Movement.R)

    assert rover.x == x and rover.y == y and rover.direction == final_direction
    
def test_bulk_move():
    movements = [Movement.F, Movement.L, Movement.F, Movement.L, Movement.B, Movement.R]
    rover = Rover(0, 0, Direction.N)
    rover.bulk_move(movements)
    
    assert rover.x == -1 and rover.y == 2 and rover.direction == Direction.W