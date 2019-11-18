import color, cstring
def main():
    print("ANSI colors available:")
    for color in Color:
        if(not (color.name in {'HEAD', 'TAIL'})): print("\t" + CString(color, color.name))

if __name__ == '__main__': main()
