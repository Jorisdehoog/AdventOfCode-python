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
i = 1
for item in data:
    x = item[0]
    # print(x)
    y = item[1]
    # coordinates are reversed
    grid[y][x] = (i)
    i += 1


# print(grid)
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        # print([i, j])
        # print(grid[i, j])
        # get the distance from the point to the populated items
        totaldis = 0
        for index, item in enumerate(data):
            totaldis += distance([i, j], item)
            if totaldis > 10000:
                break
        if index == len(data)-1 and totaldis < 10000:
            grid[i, j] = -1


# count the number of '-1'
nummin = np.where(grid.flatten() == -1)[0]
print(len(np.asarray(nummin)))

