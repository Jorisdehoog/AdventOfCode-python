# minute at asleep = this minute is sleeping
# minute at await = this minute is awake
import pprint
import re
from dateutil import parser
from operator import itemgetter
from collections import defaultdict

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
    if 'wakes' in elem:
        awoken = True
        awake = True

    awake = False
    if 'begins' in elem:
        awake = True
    
    return date, message , guard, awoken, awake


pp = pprint.PrettyPrinter()
# main logic
if __name__ == '__main__':
    sortedList = sorted(data)
    pp.pprint(sortedList)
    # loop over the input and parse the elements
    # keep a list of guards, asleep times
    # i need to keep in mind that we look for the time a guard will likely be asleep
    schedule = defaultdict(int)

    # keep track of current guard
    currentGuard = None
    awake = True
    for item in data:
        date, msg, guard, awoken, awake = inputParser(item)
        # print("date: {} -- message: {}".format(date, msg))
        # we don't want None in our dict keys
        # begin indicates awake
        # asleep indicates asleep duh
        # need to update the dict
        if guard:
            currentGuard = int(guard)
        if awoken:
            # guard has fallen asleep, subtract the previous awake time
            lastAsleep = schedule[currentGuard]['sleeptime']
            schedule[currentGuard] = {'asleeptime' : date - lastAsleep }
            schedule[currentGuard]
            # pp.pprint(schedule)

        if awake:
            # update the dict
            schedule[currentGuard].update({'guard': currentGuard,
                                'awake': awake,
                                'asleep': False,
                                'activetime': date })
        if not awake:
            schedule[currentGuard] = {'guard': currentGuard,
                                'awake': False,
                                'asleep': not awake,
                                'sleeptime': date }

    pp.pprint(schedule)