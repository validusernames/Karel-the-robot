"""
File: PotholeFilling.py
Name: Chris
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre_condition: Karel is at the (2,1), the three potholes are empty
    post_condition: Karel is at the (2,7), each pothole has 99 beepers in it
    """
    for i in range(3):
        put_99_beepersinhole()


def turn_right():
    """
    Karel turns right
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    Karel turns 180 degrees
    """
    turn_left()
    turn_left()


def put_99_beepers():
    """
    Karel drops 99 beepers
    """
    for i in range(99):
        put_beeper()


def put_99_beepersinhole():
    """
    pre_condition: Karel is at the upper left of the pothole,facing East, the pothole is empty
    post_condition: Karel is at the upper right of the pothole, facing East, the pothole has 99 beepers in it
    """
    move()
    turn_right()
    move()
    put_99_beepers()
    turn_around()
    move()
    turn_right()
    move()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
