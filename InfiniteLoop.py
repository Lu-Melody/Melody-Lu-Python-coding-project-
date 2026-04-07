"""
File: InfiniteLoop.py
Name:
------------------------
This program demonstrates the idea of an
infinite loop.

Through this example, we will observe how
a while loop can run forever if its stopping
condition is not properly designed. This
program serves as a reminder of one common
bug when using while loops.
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
