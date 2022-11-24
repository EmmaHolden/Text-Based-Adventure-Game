import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def move_on():
    move_on = False
    while not move_on:
        next = input("\nPress enter to continue.\n")
        if next == "":
            move_on = True
            clear()
