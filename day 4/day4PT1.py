import re
from dateutil import parser
from collections import defaultdict
from collections import Counter


infile = open(r'day 4\input', 'r', newline='\r\n')
data = infile.read().splitlines()

def inputParser(elem):
    # parse the time
    date = re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}\:\d{2}', elem)
    date = str(date.group())
    date = parser.parse(date)

    # get the string after the datetime
    message = re.search(r'\](.*)', elem)
    message = str(message.group(1)).strip()

    # parse the guard
    guard = re.search(r'\d*(?=\sbegins)', elem)
    if guard:
        guard = guard.group()
        # print("Guard: {}".format(guard))
    else:
        guard = None

    return date, message , guard

# main logic
if __name__ == '__main__':
    sortedList = sorted(data)
    # loop over the input and parse the elements
    # keep a list of guards, asleep times
    guardsleeping = defaultdict(list)
    guardminutes = defaultdict(list)

    # keep track of current guard
    currentGuard = None
    for item in sortedList:
        date, msg, guard = inputParser(item)

        if guard:
            currentGuard = guard
        if currentGuard not in guardsleeping:
            guardsleeping[currentGuard] = 0
        if 'falls' in msg:
            sleeptime = date
        if 'wakes' in msg:
            sleepdelta = date - sleeptime
            guardsleeping[currentGuard] += sleepdelta.seconds/60
            # keep track of the minutes the guard was sleeping
            guardminutes[currentGuard].append(list(range(sleeptime.minute, date.minute+1)))

    
    # get the highest value in the guardSleeping dict
    maxi = max(guardsleeping.keys(), key=(lambda key: guardsleeping[key]))
    print('Guard {} slept the longest with {} minutes'.format(maxi, guardsleeping[maxi]))

    # we know what guard slept the longest, now get the most common minute
    allminutes = guardminutes[maxi]
    # flatten this list
    allmin = [item for sublist in allminutes for item in sublist]
    # use the counter to get the first most common item
    mostsleptmin, mostsleptnum = Counter(allmin).most_common(1)[0]

    # we only need to multiply with the guard number now
    answer = int(maxi) * int(mostsleptmin)
    print('Answer PT1: {}'.format(answer))

    # loop over the guardminutes, get the occurrences of the minutes and find the max for each guard
    maxnum = 0
    sleepyguard = 0
    sleepyminute = 0
    for item in guardminutes:
        tempguard = item
        slept = [p for sublist in guardminutes[item] for p in sublist]
        sleptmin, sleptnum = Counter(slept).most_common(1)[0]
        if sleptnum > maxnum:
            sleepyguard = item
            sleepyminute = sleptmin
            maxnum = sleptnum
        print("Guard {} slept minute {} for {} times".format(item, sleptmin, sleptnum))
    # get the answer
    answer2 = int(sleepyguard) * int(sleepyminute)
    print('Guard {} slept during minute {} for {} times, answer is {}'.format(sleepyguard, sleepyminute, maxnum, answer2))

