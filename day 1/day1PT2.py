# do the calibration

# while looping trough the list, find the first frequency that is repeated. 
# it may be that the input list is looped over many times

# let's test first: 
# data = [+7, +7, -2, -7, -4]

import itertools

freq = 0
freqList = []
working = True
# i is the loop index
i = 0

with open(r'day 1\input', 'r', newline='\r\n') as infile:
    # data = infile.read().splitlines()
    data = [+7, +7, -2, -7, -4]
    # do the thing
    while working == True:
        for item in data:
            freq += int(item)
            if freq in freqList:
                working = False
                break
            else:
                freqList.append(freq)
                working = True

    print(freq)
    print(freqList)