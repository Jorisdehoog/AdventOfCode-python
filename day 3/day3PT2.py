import re
import numpy as np

infile = open(r'day 3\input', 'r', newline='\r\n')
data = infile.read().splitlines()

canvas = np.zeros((1000, 1000))
idcanvas = canvas.copy()

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
    

# we loop through the claims again, checking if all elements from this claim are equal to 1 
# 
# we can also nicely slice the matrix
for element in data:
    idClaim, startPos, claimSize = getInfoFromInput(element)
    # get the contents of the specific patch of the canvas
    canvasSlice = canvas[startPos[1]: startPos[1] + claimSize[1], startPos[0]: startPos[0] + claimSize[0]]
    
    # if the max is > 1 or all zeros, we know for sure it's not the match
    if np.amax(canvasSlice) > 1 or np.count_nonzero(canvasSlice) == 0:
        continue
    else:
        print('Is this the match? {}'.format(idClaim))