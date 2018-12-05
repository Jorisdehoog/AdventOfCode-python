# Scrape the contents of the puzzle input page
import urllib3

# I need to log in to get the puzzle input


# instanciate a poolmanager to make requests
http = urllib3.PoolManager()

r = http.request('GET', 'https://adventofcode.com/2018/day/1/input')

print(r.data)
