#!/usr/bin/env python3
import os
import sys

for f in os.listdir('.'):
    if os.path.isfile(f):
        print(f"{os.path.getsize(f):>8}  {f}")
