# do the calibration

# while looping trough the list, find the first frequency that is repeated. 
# it may be that the input list is looped over many times

# let's test first: 
# data = [+7, +7, -2, -7, -4]

import itertools

infile = open(r'day 1\input', 'r', newline='\r\n')

# definitions
freq = 0
loops = 0
freqList = []
elements = []
working = True
# i is the loop index
i = 0

# I want to know how many loops are done, so here's a function
def findSublist(a, b, l):
    if len(a) > len(b):
        return False
    # if l == 0: 
    for i in range(0, len(b) - len(a) + 1):
        print(b[i: i + len(a)-1])
        if b[i: i + len(a)] == a:
            return True
    # else: 
    #     for i in range(l, )
        
    return False

# data = infile.read().splitlines()
data = [+2, +2, -1, -7, -4, -3, 5 , -1, -11]
# do the thing
while working == True:
    for item in data:
        elements.append(item)
        freq += item
        if freq in freqList:
            working = False
            break
        else:
            freqList.append(freq)
            if findSublist(data, elements, loops):
                loops += 1
                print("Looped {} time(s)".format(str(loops)))
            working = True

print('Answer found: {}'.format(freq))
print(freqList)
# print(data)
print(elements)