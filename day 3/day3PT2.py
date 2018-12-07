# canvas of at least 1000X1000. Every elf claims a square of a certain width and height, and coordinates for the top-left starting point
# we need to figure out how many 'squares' are overlapping when all claims are used

# import statements
import re
import numpy as np

infile = open(r'day 3\input', 'r', newline='\r\n')
data = infile.read().splitlines()

data = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2"
]

# the canvas is at least 1000*1000 large, but it could be larger? Looking at the input data it seems to not exceed this limit
# canvas = np.zeros((1000, 1000))
canvas = np.zeros((10, 10))

def getInfoFromInput(str):
    # get the id
    # two steps: first get the pound + following number
    idFirst = re.search(r'#[0-9]*', str)
    # second step: get everything behind the pound sign (alternatively, get everything that is not a pound sign)
    idClaim = re.search(r'[^#][0-9]*', idFirst.group())
    idClaim = int(idClaim.group())

    # this gets the starting positions
    startPos = re.search(r'\d*\,\d*', str)
    startPos = startPos.group()
    startPos = startPos.split(',')
    startPos = [int(i) for i in startPos]

    # get the size of each canvas
    canvasSize = re.search(r'\d*x\d*', str)
    canvasSize = canvasSize.group()
    canvasSize = canvasSize.split('x')
    canvasSize = [int(i) for i in canvasSize]

    # return everything
    return idClaim, startPos, canvasSize


for element in data:
    idClaim, startPos, claimSize = getInfoFromInput(element)
    # start populating the canvas
    canvas[startPos[1]: startPos[1] + claimSize[1], startPos[0]: startPos[0] + claimSize[0]] += 1
    
# print(canvas[500:510, 500:510])
print(canvas)
overlap = np.where(canvas >= 2)

print('Overlapping squares: {}'.format(len(overlap[0])))

# we can loop through the claims again, checking if all elements from this claim are equal to 1 
# (meaning sum of the contents == multiplication of the sizes of the claim)
# we can also nicely slice the matrix

