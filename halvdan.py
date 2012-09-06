#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TEXT EDITOR THINGY USING CURSES IN PYTHON

import curses, locale, re

def main(stdscr):
    # Dear old int main() :D

    try:
        import terminal_info
        w,h = terminal_info.terminal_size()
    except:
        w = 80
        h = 24
    ws = str(w)
    hs = str(h)
    scr = curses.newwin(h - 1, w, 0, 0) 
    bar = curses.newwin(1, w, h - 1, 0)

    on_scr = True
    cmd = {}
#    cmd[str(229)] = insert_ch(scr, 'å')

    filename = 'test.txt'
    with open(filename) as f:
        text = f.read()
    
    # Helpful regexes and things by nycz
    lines = re.split(r'(\n)', text)
    zippedlines = zip(lines[::2], lines[1::2] + [''])
    lines2 = [t + nl for t, nl in zippedlines]
    chunks = ''.join(lines2)

    bar.addstr('>>> Status-bar H*W >>> ' + hs + '*' + ws, curses.A_REVERSE)

    for c in chunks:
        scr.addstr(c)
    scr.noutrefresh()
    bar.noutrefresh()
    curses.doupdate()

    
    while True:
        ch = scr.getch() #NOTE ch is an int; chr(ch) returns string
#        if ch == ord('q'): break
        if on_scr and ch in cmd:
            cmd[ch]
        else:
            if on_scr:
                insert_ch(scr, chr(ch))
#        else:
#            # handle statusbar command
#            pass
        scr.noutrefresh()
        bar.noutrefresh()
        curses.doupdate()


def insert_ch(win, char):
    win.addstr(char)            

def exit():
    pass


# This thingy is supposed to fix all the initscr() and noecho() and so on
# Go, go, gadget-wrapper!
locale.setlocale(locale.LC_ALL, '')
curses.wrapper(main)


#TODO stop the evil ASCII?
#TODO Enable move between status bar and screen
#TODO Enable moving on screen
#TODO Possibly think about putting a resize thingy among the refreshes
