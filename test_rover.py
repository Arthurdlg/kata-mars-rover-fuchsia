import pytest

from rover import Rover

@pytest.mark.parametrize("direction,destination_x,destination_y", 
                         [('N',0,1),
                          ('S',0,-1),
                          ('E',1,0),
                          ('W',-1,0)]
                        )
def test_move_forward(direction,
                      destination_x,
                      destination_y
                      ):
    rover = Rover(0, 0, direction)
    rover.move_forward()
    
    assert rover.x == destination_x and rover.y == destination_y and rover.direction == direction

@pytest.mark.parametrize("direction,destination_x,destination_y",
                         [('N',0,-1),
                          ('S',0,1),
                          ('E',-1,0),
                          ('W',1,0)]
                         )
def test_move_backward(direction,
                      destination_x,
                      destination_y
                      ):
    rover = Rover(0,0, direction)
    rover.move_backward()
    
    assert rover.x == destination_x and rover.y == destination_y and rover.direction == direction