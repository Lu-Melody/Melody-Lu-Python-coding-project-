"""
File: Steeplechase.py
Name: Melody Lu
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    pass
    for i in range(11):# repeat for 11 times move or jump
        if front_is_clear():
            move()
        else:
            jump()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    up()
    down()

def up():
    turn_left()
    # pre:east
    # post:north
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()

def down():
    # pre:south
    # post:east
    while front_is_clear():
        move()
    turn_left()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
