#!/usr/bin/env python3

for i in range(2, 51):
    if not(i % 3) and not(i % 5):
        print("Three + Five")
    elif not (i % 3):
        print("Three")
    elif not(i % 5):
        print("Five")
    else:
        print(i)
