#!/bin/python3
import sys

n = int(input().strip())
strings = []
for i in range(0, n):
    string = input().strip()
    strings.append(string)
    arr = list(strings[i])
    odd = []
    even = []
    for j in range(0, len(arr)):
        if j % 2 == 0:
            even.append(arr[j])
        else:
            odd.append(arr[j])
    print(''.join(even),''.join(odd))
