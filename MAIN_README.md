# Mars Rover Kata



## Your Task

You’re part of the team that explores Mars by sending remotely
controlled vehicles to the surface of the planet. You'll need to write
some code to translate the commands sent from earth to instructions that
are understood by the rover.

## Requirements

* You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
* The rover receives a character array of commands.
* Implement commands that move the rover forward/backward (f,b).
* Implement commands that turn the rover left/right (l,r).
* Implement wrapping at edges.
* Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, aborts the sequence and reports the obstacle.

## Instructions

* Draw an UML architecture by thinking hard about the project (but don't implement anything yet!)
* Link to [Class Diagram](https://drive.google.com/file/d/1s8drVCZAKpE2D3ioE4OqyuZFQvnuJ6D_/view?usp=drive_link)
 
 * Try to apply BDD:
    * Find a domain expert
    * Write test scenarios together

* Implement the test scenarios one by one, following this cycle for each feature:

1. Write the scenario (you can use the `.feature` extension if you want)
1. Write the automatic test
1. Write the production code

* Compare your architecture with what you designed

## Credits

Inspired by:  https://kata-log.rocks/mars-rover-kata (but the instructions here are slightly different)

