# do the calibration

# while looping trough the list, find the first frequency that is repeated. 
# it may be that the input list is looped over many times

# it also seems that this solution takes around 78 seconds on my machine to complete...

import time

# start timer
startTime = time.time()

infile = open(r'day 1\input', 'r', newline='\r\n')

# definitions
freq = 0
freqList = []
working = True

data = infile.read().splitlines()
# do the thing
while working == True:
    for item in data:
        item = int(item)
        freq += item
        if freq in freqList:
            working = False
            break
        else:
            freqList.append(freq)
            working = True

print('Answer found: {}'.format(freq))
print('Execution time: {} seconds'.format(time.time() - startTime))