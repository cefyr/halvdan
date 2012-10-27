#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TEXT EDITOR THINGY USING CURSES IN PYTHON

import curses, locale, re

def main(stdscr):
    # Dear old int main(), how I love thee :D

    try:
        import terminal_info
        w,h = terminal_info.terminal_size()
    except:
        w = 80
        h = 24
    ws = str(w)
    hs = str(h)
    # Cursor positions
    scr_pos = [0,0] #NOTE order of y,x
    bar_pos = 0
    bar_end = w - 20
    # win(height, width, starty, startx)
    scr = curses.newwin(h - 1, w, 0, 0) 
    bar = curses.newwin(1, w, h - 1, 0)

    on_scr = True
#    cmd = dict({'ESC':'mv_focus(on_scr)'}) #TODO change ESC to correct int
#    ch_extra = dict({196:'Ä', 197:'Å', 214:'Ö', 228:'ä', 229:'å', 246:'ö'}) 
#   ch_extra = dict({'Ã ':'Ä', 'Ã ':'Å', 'Ã ':'Ö', 'Ã¤':'ä', 'Ã¥':'å', 'Ã¶':'ö'}) 

    filename = 'test.txt'
    with open(filename) as f:
        text = f.read()
    
    # Helpful regexes and things by nycz
    lines = re.split(r'(\n)', text)
    zippedlines = zip(lines[::2], lines[1::2] + [''])
    lines2 = [t + nl for t, nl in zippedlines]
    chunks = ''.join(lines2)

    bar.addstr('>>> Status-bar H*W >>> ' + hs + '*' + ws)
#    bar.addwstr('>>> Status-bar H*W >>> ' + hs + '*' + ws, curses.A_REVERSE)

    for c in chunks:
        scr.addstr(c)
#        scr.addwstr(c)

    scr_pos[0],scr_pos[1] = scr.getyx()
# addstr coords for scr at bar_end
#    bar.addstr(0, bar_end, '{},{}'.format(scr_pos[0] + 1, scr_pos[1] + 1))
#    scr.move(scr_pos[0], scr_pos[1])
    curses.curs_set(2)
    scr.noutrefresh()
    bar.noutrefresh()
    curses.doupdate()

    
    while True:
        # TODO I think it's scr.get_wchar() etc in Python 3.3
        ch = scr.getch() #NOTE ch is an int; chr(ch) returns string
#        ch = scr.get_wch() #NOTE ch is an int; chr(ch) returns string
#        if ch == ord('q'): break
        if ch == ord('q'): #TODO Change to correct int
            if on_scr:
                bar.move(0, bar_pos)
                on_scr = False
            if not on_scr:
                #move cursor to scr in right position
                scr.move(scr_pos[0], scr_pos[1])
                on_scr = True

        else:
            if on_scr:
                insert_ch(scr, ch)
                scr_pos[0], scr_pos[1] = scr.getyx()
                bar.addstr(0, bar_end, '{},{} '.format(scr_pos[0] + 1, scr_pos[1] + 1))
                scr.move(scr_pos[0], scr_pos[1])
            if not on_scr:
                insert_ch(bar, ch)
                bar_pos = bar.getyx()[1]
#        else:
#            # handle statusbar command
#            pass
        
        scr.noutrefresh()
        bar.noutrefresh()
        curses.doupdate()


def insert_ch(win, char):
    win.addstr(chr(char))            
#    win.addwstr(chr(char))            
    # add cursor thingy


def exit():
    pass


# This thingy is supposed to fix all the initscr() and noecho() and so on
# Go, go, gadget-wrapper!
locale.setlocale(locale.LC_ALL, '')
curses.wrapper(main)


#TODO stop the evil ASCII? NOTE This might be fixed in python 3.3
#TODO Enable move between status bar and screen
#TODO Enable moving on screen
#TODO Possibly think about putting a resize thingy among the refreshes

#NOTE bar_end coords show the coords of the bar_end itself, not the place it was at before it added itself.
