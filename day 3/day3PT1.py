# canvas of at least 1000X1000. Every elf claims a square of a certain width and height, and coordinates for the top-left starting point
# we need to figure out how many 'squares' are overlapping when all claims are used

# import statements
import re

# example input
data = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2"
]

# step 1: get the info from the input strings
str = data[0]

# get the id
# two steps: first get the pound + following number
idFirst = re.search(r'#[0-9]*', str)
# second step: get everything behind the pound sign (alternatively, get everything that is not a pound sign)
idClaim = re.search(r'[^#][0-9]*', idFirst.group())
print(idClaim.group())

# this gets the starting positions
startPos = re.search(r'\d*\,\d*', str)
startPos = startPos.group()
# split up into respective parts, separated by ','
startPos = startPos.split(',')
# special loop thing
startPos = [int(i) for i in startPos]
print(startPos)

# get the size of each canvas
canvasSize = re.search(r'\d*x\d*', str)
canvasSize = canvasSize.group()
# same as above
canvasSize = canvasSize.split('x')
canvasSize = [int(i) for i in canvasSize]
print(canvasSize)
