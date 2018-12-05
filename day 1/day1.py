# first day challenge: https://adventofcode.com/2018/day/1

# add all elements form the input file together

with open(r'day 1\input', 'r', newline='\r\n') as infile:
    data = infile.read().splitlines()
    answer = 0
    for item in data: 
        answer += int(item)
print(answer)