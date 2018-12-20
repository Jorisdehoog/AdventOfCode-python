import numpy as np
import re

# get the input
infile = open(r'day 6\input2', 'r', newline='\r\n')
datastr = infile.read().splitlines()


def distance(co1, co2):
    # co1 and co2 are two points with two coordinates
    return abs(co1[0] - co2[0]) + abs(co1[1] - co2[1])

# parse the input data
data = []
for item in datastr:
    res = re.findall(r'\d+', item)
    item1 = int(res[0])
    item2 = int(res[1])
    data.append([item1, item2])

# convert to numpy array
data = np.array(data)

# get the max size of the canvas so we can init the zero matrix
xsize = max(data[:, 0])
ysize = max(data[:, 1])
print("max x: {}, max y: {}".format(xsize, ysize))

# init zero matrix
grid = np.zeros([ysize + 2, xsize + 2], int)

# 1) loop over the input data, and populate the grid with the coordinates
# 2) go over list again. go through the grid. everytime we encounter a spot
# search for next point
# (length fill = manhattan distance)
i = 11
for item in data:
    x = item[0]
    # print(x)
    y = item[1]
    # coordinates are reversed
    grid[y][x] = (i)
    i += 1

# loop over the coordinates again, and for each point fill in another 'ring' around the original point?
# no, loop over the points and calculate the manhattan distance to all other points. Fill in with the number
# of the closest point
print(len(data))

for idx, item in enumerate(data):
    # find all the distances to the other items in data
    # print(idx, item)
    # create list of indices
    looplist = list(range(0, len(data)))
    del looplist[idx]
    # print(looplist)
    totaldis = 0
    for i in looplist:
        # get the distances
        totaldis += distance(item, data[i])
        # print(totaldis)
    if totaldis < 32:
        print("{} is a good one!".format(grid[item[1]][item[0]]))
    else: 
        print("{} is a bad one!".format(grid[item[1]][item[0]]))

# remark: i still need to make the list of all valid areas using the solution for pt1
# i can probably make this more efficient though, i botched that one pretty badly