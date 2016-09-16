#!/usr/local/bin/python3
import time
import random

import curses

names = [
    'Aske',
    'Benedikt',
    'Daniel',
    'Erik',
    'Fernando',
    'Gasper',
    'Janos',
    'John',
    'Luis',
    'Lukas',
    'Markus',
    'Michael C.',
    'Michael H.',
    'Michiel',
    'Niklas',
    'Rafal',
    'Richard',
    'Tim S.',
    'Tim Z.',
    'Tobias',
    'Tom',
    'Wassim',
    'Yacha',
]

max_name_length = max(map(len, names))

names = [name.rjust(max_name_length) for name in names]

rand_names = []

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.start_color()  # init colors: 0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white

    sleep_time = 0.01
    sleep_slow_down = 1.1

    for _ in range(23):
        names_set = set(names)
        rand_names[:] = random.sample(names_set, 3)
        rand_colors = random.sample(range(1,7), 3)
        for i in range(3):
            time.sleep(sleep_time)
            stdscr.addstr(0, (max_name_length + 1) * i, rand_names[i], rand_colors[i])
            stdscr.refresh()
        sleep_time = sleep_time * (sleep_slow_down + sleep_time)
    stdscr.addstr(0, (max_name_length + 1) * 3, "🎉 ")

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)

print(" ".join(rand_names))
