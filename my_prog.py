#!/usr/bin/python3

import time

def superFunc(x):
    time.sleep(3)
    return 42

x=1
y=superFunc(x)
print(f"For x={x}, y={y}")

