# minute at asleep = this minute is sleeping
# minute at await = this minute is awake
import pprint
import re
from dateutil import parser

# test data: 
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

data = [
    "[1518-05-11 00:47] wakes up",
    "[1518-07-13 00:59] wakes up",
    "[1518-06-16 00:49] falls asleep",
    "[1518-08-17 00:01] Guard #3529 begins shift",
    "[1518-07-07 00:21] falls asleep",
    "[1518-03-28 23:56] Guard #1069 begins shift",
    "[1518-08-03 00:04] Guard #3137 begins shift",
    "[1518-04-21 00:56] wakes up",
    "[1518-07-20 00:10] wakes up",
    "[1518-11-17 00:04] Guard #1747 begins shift",
    "[1518-07-14 00:00] Guard #829 begins shift",
    "[1518-03-11 00:56] wakes up",
    "[1518-11-16 00:22] falls asleep",
    "[1518-07-15 00:56] falls asleep",
    "[1518-03-18 00:22] wakes up",
    "[1518-04-26 00:41] wakes up",
    "[1518-04-05 23:59] Guard #2287 begins shift",
    "[1518-06-20 00:20] falls asleep",
    "[1518-08-10 00:55] wakes up",
    "[1518-10-28 00:59] wakes up",
    "[1518-09-09 00:27] falls asleep"
]

def inputParser(elem):
    # parse the time
    date = re.search(r'\d{4}-\d{2}-\d{2}\s\d{2}\:\d{2}', elem)
    date = str(date.group())
    date = parser.parse(date)
    # print(date.minute)

    # parse the guard
    guard = re.search(r'\d*(?=\sbegins)', elem)
    if guard:
        guard = guard.group()
        # print("Guard: {}".format(guard))
    else:
        guard = None
    
    # get the state of the guard
    awake = False
    if 'begins' in elem or 'wakes' in elem:
        awake = True
    
    return date, guard, awake

# sortedList:
# [[date, string],[date, string],[date, string],...]

# order the input list
def sortInput(data):
    sortedList = []
    # date-items can directly be compared
    for item in data:
        date = inputParser(item)
        # insert the first element into the sorted list
        if not sortedList:
            sortedList.append([date, item])
            continue
        print('---- input date ----')
        print(date)

        for i in range(0, len(sortedList)):
            print('---- list date ----')
            print(sortedList[0][i])
            if date < sortedList[0][i]:
                print(' nothin')


# sort the input
sortInput(data)

# keep track of current guard
guardCurrent = '0'
# # main loop
# orderedData = {
#     'month': 0,
#     'day': 0,
# }


for item in data:
    date, guard, awake = inputParser(item)
    # order list while inserting into orderedList
    # we know that the year is constant, but month and day vary
    


    # not needed yet
    if not guard:
        guard = guardCurrent
    if guard or awake:
        guardCurrent = guard
        print('Guard {} awake? {}. Minute is {}'.format(guard, awake, date.minute))
    else:
        print('Guard is sleeping')
