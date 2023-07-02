import sys
import time

def ft_progress(lst):
    current = time.time()
    for i in range(len(lst)): # attention range prend un int comme arg donc pas directement une liste
        sys.stdout.write('\r') #The '\r' character (carriage return) resets the cursor to the beginning of the line and allows you to write over what was previously on the line
        sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * i / len(lst)), (i + 1) / len(lst) * 100))
        sys.stdout.write(" | elapsed time %d seconds" % (time.time() - current))
        sys.stdout.flush()
        yield i
    i += 1

def main():
    listy = range(100)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)

if __name__ == "__main__":
    main()

sys.exit(1)

# https://www.geeksforgeeks.org/sys-stdout-write-in-python/ :
# stdout is used to display output directly to the screen console
# Unlike print, sys.stdout.write doesn’t switch to a new line after one text is displayed


# faire une toolbar:
# https://stackoverflow.com/questions/3002085/how-to-print-out-status-bar-and-percentage