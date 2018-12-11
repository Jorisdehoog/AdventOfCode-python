# minute at asleep = this minute is sleeping
# minute at await = this minute is awake
import pprint
import re
from dateutil import parser
from operator import itemgetter

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
    awake = False
    if 'begins' in elem or 'wakes' in elem:
        awake = True
    
    return date, message #, guard, awake

    
# sort the input
# separateInput(data)

pp = pprint.PrettyPrinter()
# this works...
pp.pprint(sorted(data))

