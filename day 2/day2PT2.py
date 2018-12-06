# the input data contains a bunch of strings. We need to find the two strings that differ in exactly 
# one character on the exact same place. Then we need to find the corresponding letters


# loop over list, compare all following items to the considered file
# for each item, transform it into a list of letters, keeping the order
# count the number of matching elements. If this is less than len(item) - 1
# we automatically reject. If the difference is exactly one, we know we found the match

infile = open(r'day 2\input', 'r', newline='\r\n')
data = infile.read().splitlines()

for i in range(0, len(data)):
    itemList = list(data[i])

    # look im doing list comprehension!
    itemListOrd = [ord(p)-96 for p in itemList]

    # look for all following items
    for j in range(i+1, len(data)):
        itemCheck = list(data[j])
        # convert to numbers so we can subtract these lists from each other to find the 'pattern'
        itemCheckOrd = [ord(p)-96 for p in itemCheck]
        # subtract both. If the list of unique items in total is exactly one item long, we have found our match 
        total = []
        for x, y in zip(itemListOrd, itemCheckOrd):
            total.append(x-y)
        # remove the zeros
        totalNoZero = [p for p in total if p != 0]
        if len(totalNoZero) == 1:
            print("{} AND {}".format(data[i], data[j]))
            # find the index of the nonzero element in total
            index = total.index(totalNoZero[0])
            # correspondingLetters = itemList.pop(index)
            itemList.pop(index)
            print('we found it!')
            print('Answer: {}'.format(''.join(itemList)))

# Thoughts: I don't stop the loop when the match is found.
# Let's say it's simply to check wether or not we have a good input set
# and not accidentaly more than one match :)