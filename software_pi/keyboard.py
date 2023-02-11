import sys, tty, termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    key = getch()
    if key == '\r':
        print("Enter key pressed")
    elif key == '\x1b':
        print("Escape key pressed")
        break
    else:
        print("Key pressed: ", key)
