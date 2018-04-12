#!/bin/python3

import sys

inputs = []

n = int(input().strip())

for i in range(0, n):
    entry = (input().strip())
    contact = entry.split(' ')
    inputs.append(contact)
    
dictionary = dict(inputs)

for i in range(0, n):
    entry = (input().strip())
    number = dictionary.get(entry)
    if number == None:
        print("Not found")
    else:
        print("%s=%s" % (entry, number))
