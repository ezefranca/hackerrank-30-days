#!/bin/python3
import sys

n = int(input().strip())
if n >= 2 and n <= 20:
    for i in range(1,11):
     print(n,'x',i,'=',n*i)
