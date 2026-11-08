#!/usr/bin/env python3
"""Print the current time. A small clock."""
import time
import datetime

def main():
    while True:
        now = datetime.datetime.now()
        print(now.strftime('%Y-%m-%d %H:%M:%S'), end='\r')
        time.sleep(1)

if __name__ == '__main__':
    main()
