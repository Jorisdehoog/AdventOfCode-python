# apparently this repo was not pushed to github, so ill do it again
from collections import defaultdict

# test file
data = 'dabAcCaCBAcCcaDA'

# input
infile = open(r'day 5\input', 'r')
data = infile.read().strip('\n')


def getFinishedPoly(data):
    i = 0
    while i <= len(data):
        try:
            a = data[i]
            b = data[i + 1]
        except IndexError:
            break

        if a.swapcase() == b:
            del data[i:i + 2]
            # two steps back
            i = i - 2
            # avoid index error
            if i < 0: 
                i = 0
        else:
            i += 1

    return len(data)


# get unique elements from the lower list
datalow = list(data.lower())
dataunique = sorted(set(datalow))

data = list(data)
# keep all answers in a dict
answers = defaultdict(list)
for item in dataunique:
    # make a copy of the original data
    tempdata = data.copy()
    indices = [i for i, x in enumerate(data) if x == item.lower() or x == item.upper()]
    # do a reverse sort so we don't run into index error
    for i in sorted(indices, reverse=True):
        del tempdata[i]
    answers[item].append(getFinishedPoly(tempdata))
    print('Removed {}, final length after processing: {}'.format(item, answers[item][0]))

mini = min(answers.keys(), key=(lambda key: answers[key]))
print('-------------------------')
print('Best version: {} with length: {}'.format(mini, answers[mini][0]))

