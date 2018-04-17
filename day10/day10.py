#!/bin/python3

import sys

n = int(input().strip())
binary = list(str("{0:b}".format(n)))
count = 0
values = []
for i in binary:
    if int(i) == 1:
        count = count + 1
    else:
        values.append(count)
        count = 0      
values.append(count)
print(max(values))
