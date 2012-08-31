#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TEST AND THINGIES USING CURSES IN PYTHON

import curses

def main(stdscr):
    # Dear old int main() :D
    h = 20
    w = 80
    scr = curses.newwin(h - 1, w, 0, 0) #might have to be a pad?
    bar = curses.newwin(1, w, h - 1, 0)

    on_scr = True

    filename = '~/80char.txt'
    with open(filename) as f:
        text = f.read()
    chunks = text.split('\n')
    for c in chunks:
        scr.addstr(c)
    bar.addstr('*****EOF****', curses.A_REVERSE)
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
