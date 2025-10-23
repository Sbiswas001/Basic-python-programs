import sys

#!/usr/bin/env python3
"""Simple hello world script.

Usage:
    python helloworld.py         # -> Hello, World!
    python helloworld.py Alice   # -> Hello, Alice!
"""

def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    name = argv[0] if argv else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()