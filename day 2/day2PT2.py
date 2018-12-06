# the input data contains a bunch of strings. We need to find the two strings that differ in exactly 
# one character on the exact same place. Then we need to find the corresponding letters

data = [
    "abcde",
    "fghij",
    "klmno",
    "pqrst",
    "fguij",
    "axcye",
    "wvxyz"
]

# test something
# a = [1, 2, 3, 4, 5]
# b = [1, 2, 9, 8, 5]
# total = []
# for x, y in zip(a, b):
#     total.append(x - y)

# # remove the zeros
# total = [p for p in total if p != 0]
# print(len(total))

# loop over list, compare all following items to the considered file
# for each item, transform it into a list of letters, keeping the order
# count the number of matching elements. If this is less than len(item) - 1
# we automatically reject. If the difference is exactly one, we know we found the match

print('length of the input array: {}'.format(len(data)))

for i in range(0, len(data)):
    itemList = list(data[i])
    # look im doing list comprehension!
    itemListOrd = [ord(p)-96 for p in itemList]
    print('-- {} --'.format(itemList))

    print(itemList)
    # look for all following items
    for j in range(i+1, len(data)):
        itemCheck = list(data[j])
        itemCheckOrd = [ord(p)-96 for p in itemCheck]
        # use zip to loop over the two lists?
        total = []
        for x, y in zip(itemListOrd, itemCheckOrd):
            total.append(x-y)
        # remove the zeros
        total = [p for p in total if p != 0]
        if len(total) == 1:
            print("{} AND {}".format(data[i], data[j]))
            print('we found it!')


        
        
        # find what positions match the itemList


