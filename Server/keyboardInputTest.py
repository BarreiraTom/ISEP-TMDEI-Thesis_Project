#
# ONLY WORKS ON LINUX!!!!
#
import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print ("up\n")
        elif char == curses.KEY_DOWN:
            print ("down\n")
        elif char == curses.KEY_RIGHT:
            print ("right\n")
        elif char == curses.KEY_LEFT:
            print ("left\n")
        elif char == 10:
            print ("stop\n")

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
