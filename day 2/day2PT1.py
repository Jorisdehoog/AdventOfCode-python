# find the following groups in the input strings: 
# a letter appears exactly twice
# a letter appears exactly thrice

# im not trying regex

# open the input file
infile = open(r'day 2\input', 'r', newline='\r\n')
data = infile.read().splitlines()

# declare the variables
toos = 0
threes = 0

for item in data: 
    foundLetters = []
    # use a set
    foundLetters = list(item)
    setLetter = set(foundLetters)

    # keep track of double and triple letter combos
    foundNumbers = []
    for letter in setLetter:
        amount = foundLetters.count(letter)
        if amount == 2 or amount == 3:
            foundNumbers.append(amount)

    # check the conditions
    # make a set of the foundNumbers to filter out the doubles
    filteredNumbers = set(foundNumbers)
    if len(filteredNumbers) == 0:
        continue
    elif len(filteredNumbers) == 1:
        # get the content of the single value in the set
        val = filteredNumbers.pop()
        if val == 2:
            toos += 1
        else:
            threes += 1
    elif len(filteredNumbers) > 1:
        # add one to both
        toos += 1
        threes += 1

print("Result is: {}".format(str(toos * threes)))