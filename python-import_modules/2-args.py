#!/usr/bin/python3

import sys

def main():
    arg_count = len(sys.argv) - 1
    argument = "argument" if arg_count == 1 else "arguments"
    if arg_count == 0:
        print("0 arguments.")
    else:
        print(f"{arg_count} {argument}:")
        for index, value in enumerate(sys.argv[1:], start=1):
            print(f"{index}: {value}")
if __name__ == "__main__":
    main()
