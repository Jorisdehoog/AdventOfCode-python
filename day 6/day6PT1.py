import numpy as np
import re
import pprint

# get the input
infile = open(r'day 6\input', 'r', newline='\r\n')
datastr = infile.read().splitlines()

# init pprint
pp = pprint.PrettyPrinter()

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
# pp.pprint(grid)

# 1) loop over the input data, and populate the grid with the coordinates
# 2) go over list again. go through the grid. everytime we encounter a spot
# search for next point
# (length fill = manhattan distance)
i = 10
for item in data:
    x = item[0]
    # print(x)
    y = item[1]
    # coordinates are reversed
    grid[y][x] = (i)
    i += 1

# print(grid)

# loop over the coordinates again, and for each point fill in another 'ring' around the original point?
# no, loop over the points and calculate the manhattan distance to all other points. Fill in with the number
# of the closest point

for yax in range(0, grid.shape[1]):
    for xax in range(0, grid.shape[0]):
        # loop over coordinates:
        point = [xax, yax]
        # grid[xax, yax] = 999
        # print(grid)
        # continue
        if grid[xax, yax] != 0:
            continue

        # dislist = np.array(dislist)
        i = 1
        # init new 
        dislist = []
        # dislist = np.array(dislist)
        for item in data:
            # calculate the distance
            x1 = item[1]
            y1 = item[0]
            dis = distance(point, [x1, y1])
            # np.append([dislist], [i, dis], axis=1)
            testpoint = grid[x1, y1]
            dislist.append([testpoint, dis])
            i = i + 1
        
        # look for the min value
        dislist = np.array(dislist)
        # print(dislist[:, 1])
        mindis = min(dislist[:, 1])
        minitemindex = np.where(dislist[:, 1] == mindis)
        # print(np.asarray(minitemindex).shape)
        if np.asarray(minitemindex).shape != (1, 1):
            # we need to skip this point
            # print('opes')
            continue

        grid[xax][yax] = dislist[minitemindex, 0]
        
        # print(mindis)
    # print(grid)
print('-------------------------')
# print(grid)

# grid shape
x, y = grid.shape

# find the largest set of numbers that are contained, and not infinite (not on the edge)
uniques = np.bincount(grid.flatten())
ii = np.nonzero(uniques)[0]

solutions = []

for elem, num in zip(ii, uniques[ii]):
    test = np.where(grid == elem)
    test = np.array(test)
    # print(type(test))
    if (test == 0).any() or (test >= x-1).any() or (test >= y-1).any():
        # edge case: 
        print('{} extends to infinity'.format(elem))
    else:
        print('{} IS FINE, size = {}'.format(elem, num))
        solutions.append([elem, num])
    # print(test)
    # print(elem, num)

solutions = np.array(solutions)
print(solutions)
print(max(solutions[:, 1]))