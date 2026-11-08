#!/usr/bin/env python3

import sys

# Simple ackermann implementation to check how well Python deals with it.

iterations = 0

def ackermann(m, n):
    global iterations
    iterations += 1
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

if __name__ == "__main__":
    print("Default recursion limit:", sys.getrecursionlimit())
    
    # Try to find the breaking point for m=3
    for n in range(10):
        try:
            iterations = 0
            result = ackermann(3, n)
            print(f"m=3, n={n}: Result={result}, Iterations={iterations}")
        except RecursionError:
            print(f"m=3, n={n}: RecursionError")
            break
