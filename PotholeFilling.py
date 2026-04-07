"""
File: PotholeFilling.py
Name: Melody Lu
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *


def main():
    """
    Melody Lu
    pre:east
    post:south
    """
    pass

    def turn_right():
        turn_left()
        turn_left()
        turn_left()

    def put_99():
     for i in range(99):
        put_beeper()

    def go_in():
        move()
        turn_right()
        move()
        put_99()

    def go_out():
        turn_left()
        turn_left()
        move()
        turn_right()
        move()

    def one_time():
        for i in range(3):
            go_in()
            go_out()

    def upper_one():
        for i in range(3):
            move()
            turn_right()
            move()
            put_99()
            turn_left()
            turn_left()
            move()
            turn_right()
            move()




    one_time()
    turn_left()
    for i in range(4):
        move()
    turn_left()
    upper_one()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
