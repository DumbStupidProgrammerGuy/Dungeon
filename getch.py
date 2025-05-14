import sys
import tty
import termios
import select

def getch_with_timeout(timeout=5):
    fd = sys.stdin.fileno()
    # old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        rlist, _, _ = select.select([sys.stdin], [], [])
        if rlist:
            ch = sys.stdin.read(1)
            # print(sys.stdin.read(2))
        else:
            ch = None
        print(1)
    finally:
        # termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print(2)
    return ch

# Example usage
if __name__ == "__main__":
    while True:
        print("Press any key within 5 seconds: ")
        char = getch_with_timeout()
        if char:
            print(f"You pressed: {char},{ord(char)}")
            if ord(char) == 3:
                print("Exiting...")
                sys.exit(0)
        else:
            print("Skipped")