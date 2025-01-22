from rover import Rover


def test_get_answer():
    rover = Rover(0, 0, 'N')
    rover.move_forward()
    
    assert rover.x == 0 and rover.y == 1
