# find the following groups in the input strings: 
# a letter appears exactly twice
# a letter appears exactly thrice

# im not trying regex

data = [
    "abcdef",
    "bababc", 
    "abbcde", 
    "abcccd", 
    "aabcdd", 
    "abcdee", 
    "ababab"
]

for item in data: 
    foundLetters = []
    for letter in item: 
        index = []
        index.append(item.find(letter))
        print(index)
        
    print(item)