from ftfutils.color import *
from ftfutils.cstring import *
from ftfutils.mode import *
from ftfutils.utilities import log

def main():
    log(Mode.INFO, "ANSI colors available:")
    for c in Color:
        if(not (c.name in {'HEAD', 'TAIL'})): print("\t" + CString(c, c.name))

if __name__ == '__main__': main()
