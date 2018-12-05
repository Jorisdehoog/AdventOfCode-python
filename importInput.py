# Scrape the contents of the puzzle input page
from urllib.request import FancyURLopener

# define new class, with new user-agent
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

myopener = MyOpener()
with myopener.open('https://adventofcode.com/2018/day/1/input') as page:
    print(page.read())
