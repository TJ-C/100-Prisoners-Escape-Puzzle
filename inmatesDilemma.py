import array
from operator import truediv
import random

inmatesNumbers = range(0, 99)
inmatesNumber = list(inmatesNumbers)
boxes = list(inmatesNumbers)
random.shuffle(boxes)

cycles = 1000
totalCycles = cycles
success = 0
failure = 0
loop = []
numberInsideBox = -1
tries = 50
inmatesThatFoundTheirNumber = 0
found = False
triesPerInmate = []
firstBox = True
# 
# An inmate picks the box corresponding to his number, they then pick from the box whose number corresponds to the number they picked.
# They follows the chain until they find their number, or their number of tries runs out.
# https://datagenetics.com/blog/december42014/index.html
# 

# Perform a large number of cycles to obtain a success percentage.
while cycles > 0:
    for inmateNumber in inmatesNumber:
        # print("Searching for imate {}".format(inmateNumber))
        # Pick number from box that corresponds to inamte number
        numberInsideBox = boxes[inmateNumber]
        while tries > 0:
            if (numberInsideBox == inmateNumber):
                found = True
                triesPerInmate.append(50 - tries)
                inmatesThatFoundTheirNumber += 1
                loop.append(numberInsideBox)
                # print("found")
                # print("loop completed in {} tries".format(50 - tries))
                # print(loop)
                break
            else:
                loop.append(numberInsideBox)
                numberInsideBox = boxes[numberInsideBox]
                tries -= 1
        if  not found:
            pass
            # print("Inmate {} not found after 50 tries.".format(inmateNumber))
        else:
            found = False
        # print(tries)
        # print("tries")
        tries = 50
        loop = []
        firstBox = True
    print("Number of inmates who found their number: {}".format(inmatesThatFoundTheirNumber))

    if len(triesPerInmate) != 0:
        print("Average number of tries needed: {}".format((sum(triesPerInmate) / len(triesPerInmate))))
    else:
        print("All inmates failed to find their number")
    print("Contents of boxes: {}".format(boxes))
    if inmatesThatFoundTheirNumber == 99:
        print("All imates are set free!!!")
        success += 1
    else:
        print("All inmates are executed")
        failure += 1

    cycles -= 1
    # Reset all the variables before performing the next cycle.
    loop = []
    numberInsideBox = -1
    tries = 50
    inmatesThatFoundTheirNumber = 0
    found = False
    triesPerInmate = []
    firstBox = True
    random.shuffle(boxes)

print("Success: {} - Failure: {} pecentage sucess: {}%".format(success, failure, ((success / totalCycles) * 100)))
