#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TEST AND THINGIES USING CURSES IN PYTHON

import curses, re

def main(stdscr):
    # Dear old int main() :D
    h = 20
    w = 80
    scr = curses.newwin(h - 1, w, 0, 0) #might have to be a pad?
    bar = curses.newwin(1, w, h - 1, 0)

    on_scr = True
    #cmd = {curses.KEY_F2:break}

    filename = 'test.txt'
    with open(filename) as f:
        text = f.read()
    
    # Helpful regexes and things by nycz
    lines = re.split(r'(\n)', text)
    zippedlines = zip(lines[::2], lines[1::2] + [''])
    lines2 = [t + nl for t, nl in zippedlines]
    chunks = ''.join(lines2)

    for c in chunks:
        scr.addstr(c)
    bar.addstr('>>> Status-bar whoop whoop >>>', curses.A_REVERSE)
    scr.noutrefresh()
    bar.noutrefresh()
    curses.doupdate()

    
    while True:
        ch = scr.getch()
        if ch == ord('q'): break
                                              
        scr.noutrefresh()
        bar.noutrefresh()
        curses.doupdate()

# This thingy is supposed to fix all the initscr() and noecho() and so on
# Go, go, gadget-wrapper!
curses.wrapper(main)
