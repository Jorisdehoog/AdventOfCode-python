# minute at asleep = this minute is sleeping
# minute at await = this minute is awake
import pprint
import re
from dateutil import parser

# test data: 
data = [
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up"
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


# keep track of current guard
guardCurrent = '0'
# main loop
orderedData = {
    'month': 0,
    'day': 0,
}
for item in data:
    date, guard, awake = inputParser(item)
    # order list while inserting into orderedList
    # we know that the year is constant, but month and day vary
    month = date.month
    day = date.day


    # not needed yet
    if not guard:
        guard = guardCurrent
    if guard or awake:
        guardCurrent = guard
        print('Guard {} awake? {}. Minute is {}'.format(guard, awake, date.minute))
    else:
        print('Guard is sleeping')
