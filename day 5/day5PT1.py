# apparently this repo was not pushed to github, so ill do it again

# test file
data = 'dabAcCaCBAcCcaDA'

# input
infile = open(r'day 5\input', 'r')
data = infile.read().strip('\n')


data = list(data)

print(len(data))
print(data[-1])

i = 0
while i <= len(data):
    try:
        a = data[i]
        b = data[i + 1]
    except IndexError:
        break

    if a.swapcase() == b:
        # print(data)
        del data[i:i + 2]
        # print(data)
        # two steps back
        i = i - 2
        # avoid index error
        if i < 0: 
            i = 0
    else:
        i += 1

print(len(data))
