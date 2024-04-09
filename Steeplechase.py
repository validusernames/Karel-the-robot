"""
File: Steeplechase.py
Name: Chris
---------------------------------
Karel will jump over eleven hurdles
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    Pre-condition:Karel is at the left side of the wall
    Post-condition: Karel is at the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition: Karel is at the bottom right of the wall, facing East
    Post-condition: Karel is at the top right of the wall, facing East
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    """
    Pre-condition: Karel is at the top right of the wall, facing East
    Post-condition: Karel is at top left of the wall, facing South
    """
    move()
    turn_right()


def down():
    """
    Pre-condition: Karel is at the top left of the wall, facing South
    Post-condition:  Karel is at the bottom left of the wall, facing East
    """
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    """
    Karel will turn right 90 degrees
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    Karel will turn 180 degrees
    """
    turn_left()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
