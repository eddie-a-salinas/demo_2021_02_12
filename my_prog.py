#!/usr/bin/python3

import time

def superFunc(x):
    time.sleep(0)
    return 42

x=1
y=superFunc(x)
print(f"For x={x}, y={y}")

