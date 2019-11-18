from color import *
from cstring import *
from mode import *
from utilities import log

def main():
    log(Mode.INFO, "ANSI colors available:")
    for c in Color:
        if(not (c.name in {'HEAD', 'TAIL'})): print("\t" + CString(c, c.name))

if __name__ == '__main__': main()
