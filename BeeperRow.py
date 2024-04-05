"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    for i in range(99):
        while front_is_clear():
                put_beeper()
                move()
        turn_around()
        put_beeper()


def turn_around():
    turn_left()
    turn_left()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
