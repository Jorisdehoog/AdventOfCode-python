# do the calibration

# while looping trough the list, find the first frequency that is repeated. 
# it may be that the input list is looped over many times

# let's test first: 
data = [3, 3, 4, -2, -4]

freq = 0
freqList = []
working = True
while working == True:
    # loop over items
    for item in data:
        freq += int(item)
        if freq in freqList:
            print(freq)
            # False
            working = False
        else:
            freqList.append(freq)
            working = True
