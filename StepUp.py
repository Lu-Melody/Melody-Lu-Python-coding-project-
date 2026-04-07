"""
File: StepUp.py
Name: Melody Lu
------------------------
This program demonstrates how Karel picks up a beeper
at Street 1 Avenue 2 and moves it to Street 2 Avenue 4.

By guiding Karel step by step, we will practice writing
clear and well-structured commands. At the end of the
program, Karel will be facing East at Street 2 Avenue 5.
"""

from karel.stanfordkarel import *


def main():
    pass #pass means nothing it is here to indicate we should write from here with a tab
    move()
    pick_beeper()
    move()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_75()
def turn_right(): #definition and the main code should be seperated in any sequence
    turn_left()
    turn_left()
    turn_left()
def put_75():
    for i in range(75):
        put_beeper()





if __name__ == '__main__':
    execute_karel_task(main)
