#!/usr/bin/python3
import sys
import os

"""that takes an argument 2 strings"""

if __name__ == "__main__":
    arguments = len(sys.argv) - 1

    if arguments < 1:
        print("Usage: ./markdown2html.py README.md README.html",
        file=sys.stderr, end="")
        sys.exit(1)
    if os.path.exists(sys.argv[1]) != True:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr, end=" ")
        sys.exit(1)

    sys.exit(0)