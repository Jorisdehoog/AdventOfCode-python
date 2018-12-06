# find the following groups in the input strings: 
# a letter appears exactly twice
# a letter appears exactly thrice

# im not trying regex

data = [
    "abcdef",
    "bababc",   #counts for both, yes and yes
    "abbcde",   #
    "abcccd", 
    "aabcdd", 
    "abcdee", 
    "ababab"
]

for item in data: 
    foundLetters = []
    # use a set
    foundLetters = list(item)
    setLetter = set(foundLetters)

    print(foundLetters)
    # keep track of double and triple letter combos
    foundNumbers = []
    for letter in setLetter:
        amount = foundLetters.count(letter)
        if amount == 2 or amount == 3:
            foundNumbers.append(amount)
        
        print("Found {} {} times".format(letter, foundLetters.count(letter)))
        print('test')
        
    print(item)