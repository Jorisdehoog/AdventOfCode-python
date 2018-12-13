# minute at asleep = this minute is sleeping
# minute at await = this minute is awake
import pprint
import re
from dateutil import parser
from operator import itemgetter
from collections import defaultdict
from collections import Counter

# data = [
#     "[1518-11-01 00:00] Guard #10 begins shift",
#     "[1518-11-01 00:05] falls asleep",
#     "[1518-11-01 00:25] wakes up",
#     "[1518-11-01 00:30] falls asleep",
#     "[1518-11-01 00:55] wakes up",
#     "[1518-11-01 23:58] Guard #99 begins shift",
#     "[1518-11-02 00:40] falls asleep",
#     "[1518-11-02 00:50] wakes up",
#     "[1518-11-03 00:05] Guard #10 begins shift",
#     "[1518-11-03 00:24] falls asleep",
#     "[1518-11-03 00:29] wakes up",
#     "[1518-11-04 00:02] Guard #99 begins shift",
#     "[1518-11-04 00:36] falls asleep",
#     "[1518-11-04 00:46] wakes up",
#     "[1518-11-05 00:03] Guard #99 begins shift",
#     "[1518-11-05 00:45] falls asleep",
#     "[1518-11-05 00:55] wakes up"
# ]

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
    
    # get the state of the guard
    awoken = False
    awake = False
    if 'wakes' in elem:
        awoken = True
        awake = True

    if 'begins' in elem:
        awake = True
    
    return date, message , guard, awoken, awake


pp = pprint.PrettyPrinter()
# main logic
if __name__ == '__main__':
    sortedList = sorted(data)
    # loop over the input and parse the elements
    # keep a list of guards, asleep times
    # i need to keep in mind that we look for the time a guard will likely be asleep
    # should i use another data structure then dicts? 
    guardsleeping = defaultdict(list)
    guardminutes = defaultdict(list)

    schedule = {}

    # schedule = defaultdict(int)
    # keep track of current guard
    currentGuard = None
    for item in sortedList:
        date, msg, guard, awoken, awake = inputParser(item)
        print(item)

        if guard:
            currentGuard = guard
        if currentGuard not in guardsleeping:
            guardsleeping[currentGuard] = 0
        if 'falls' in msg:
            # print('fell asleep')
            sleeptime = date
        if 'wakes' in msg:
            # should always pass
            if sleeptime:
                sleepdelta = date - sleeptime
            else:
                print('what')
            # print(sleepdelta.seconds/60)
            guardsleeping[currentGuard] += sleepdelta.seconds/60
            # keep track of the minutes the guard was sleeping
            # print(range(sleeptime.minute, date.minute))
            guardminutes[currentGuard].append(list(range(sleeptime.minute, date.minute+1)))

    
    # get the highest value in the guardSleeping dict
    maxi = max(guardsleeping.keys(), key=(lambda key: guardsleeping[key]))
    print('Guard {} slept the longest with {} minutes'.format(maxi, guardsleeping[maxi]))

    # we know what guard slept the longest, now get the most common minute
    allminutes = guardminutes[maxi]
    # flatten this list
    allmin = [item for sublist in allminutes for item in sublist]
    # print(allminutesunion)

    # use the counter to get the first most common item
    mostsleptmin, mostsleptnum = Counter(allmin).most_common(1)[0]
    print(mostsleptmin)

    # we only need to multiply with the guard number now
    answer = int(maxi) * int(mostsleptmin)
    print('Answer: {}'.format(answer))
