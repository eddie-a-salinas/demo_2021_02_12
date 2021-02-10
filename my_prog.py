#!/usr/bin/python3

import time

def finalComp(y):
    result=y
    result+=1
    result+=1
    result+=1
    result+=1
    return result
    

def superFunc(x):
    time.sleep(3)
    return 42

x=1
y=superFunc(x)
print(f"For x={x}, y={y}")
grandResult=finalComp(y)
print(f'The final result is {grandResult} !!!')
