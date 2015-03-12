e#Starts curses
import curses
stdscr = curses.initscr()
curses.noecho(); curses.cbreak(); stdscr.keypad(1)

#Codegohere
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
addstr("hello world")

#Ends curses
#curses.nocbreak(); stdscr.keypad(0); curses.echo()
