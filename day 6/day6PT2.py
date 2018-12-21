import numpy as np
import re

# get the input
infile = open(r'day 6\input', 'r', newline='\r\n')
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

# WAIT no i misread the question: I need to loop over all the points in the grid, and if the accumulative distances to the other points are
# less than 32, mark it. 

# remark: i still need to make the list of all valid areas using the solution for pt1
# i can probably make this more efficient though, i botched that one pretty badly

# print(grid)
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        # print([i, j])
        # print(grid[i, j])
        # get the distance from the point to the populated items
        totaldis = 0
        for item in data:
            totaldis += distance([i, j], item)
        # print(totaldis)
        if totaldis < 1000:
            grid[i, j] = '-1'
        # print('')
        # dislist = np.array(dislist)
        # mindis = min(dislist[:, 1])
        # minitemindex = np.where(dislist[:, 1] == mindis)
        # if np.asarray(minitemindex).shape != (1, 1):
        #     continue
        # grid[i, j] = dislist[minitemindex, 0]
# print(grid)

# count the number of '-1'
nummin = np.where(grid.flatten() == -1)[0]
print(len(np.asarray(nummin)))

# grid shape
x, y = grid.shape

# find the largest set of numbers that are contained, and not infinite (not on the edge)
uniques = np.bincount(grid.flatten())
ii = np.nonzero(uniques)[0]

# i can replace the array with a single value and compare new found areas with this one
solutions = []
for elem, num in zip(ii, uniques[ii]):
    test = np.where(grid == elem)
    test = np.array(test)
    # this test could be better, i think i'm taking a risk here
    if (test == 0).any() or (test == x-1).any() or (test == y-1).any():
        # edge case: 
        # print('{} extends to infinity'.format(elem))
        continue
    else:
        # print('{} IS FINE, size = {}'.format(elem, num))
        solutions.append([elem, num])

solutions = np.array(solutions)
print(max(solutions[:, 1]))

""" PART 2"""

# loop over the coordinates again, and for each point fill in another 'ring' around the original point?
# no, loop over the points and calculate the manhattan distance to all other points. Fill in with the number
# of the closest point

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

print(solutions)