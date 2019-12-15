from MicroBitTools import flash
import sys
from os import getcwd


def main():
    print("works")
    args = sys.argv[1:]
    cwd = getcwd()
    pyfile = args[0]
    if args[0] is not None:
        flash(cwd+"\\"+pyfile)
    else:
        print("Error: Unable to find argument with filename")


if __name__ == '__main__':  # pragma: no cover
    main()
