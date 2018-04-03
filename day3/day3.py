#!/bin/python3

import sys
n = int(input().strip())
if (n % 2 != 0) or (n > 5 and n <= 20):
    print("Weird")
elif(n > 0 and n < 5) or (n > 20):
    print("Not Weird")
