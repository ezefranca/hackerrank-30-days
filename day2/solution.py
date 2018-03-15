#!/bin/python3

import sys
import math

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    print("The total meal cost is {} dollars.".format(round(meal_cost + (tip_percent/100) * meal_cost + (tax_percent/100) * meal_cost)))

