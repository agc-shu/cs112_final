# CS112 Final Project
# Andrew Caramore

import math


# Standard Deviation Function
def stdev(values):
    total = 0
    for number in values:
        total += float(number)
    mean = total / len(values)
    total = 0
    for number in values:
        total += (float(number) - mean) * (float(number) - mean)
    total = total / (len(values) - 1)
    return math.sqrt(total)

# Main
while True:
    strInput = input("Enter temperature values separated by a single space: ")
    values = strInput.split()
    dev = stdev(values)
    print(dev)
    if dev > 1:
        print("NOT COMFY")
    else:
        print("COMFY")