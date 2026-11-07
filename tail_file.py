#!/usr/bin/env python3
"""Print the last N lines of a file, like tail -n."""
import argparse

def tail_file(path, n):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines[-n:]

def main():
    parser = argparse.ArgumentParser(description='Print the last N lines of a file.')
    parser.add_argument('file', help='Path to the file to read')
    parser.add_argument('-n', type=int, default=10, help='Number of lines to print')
    args = parser.parse_args()

    try:
        result = tail_file(args.file, args.n)
        for line in result:
            print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    import sys
    main()
