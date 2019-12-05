# Copied from https://github.com/antooro/advent-of-code-2019/blob/master/startDay.py
# modified slightly to fit my formatting

import requests
import os
from datetime import date
import browser_cookie3
import sys

#Get cookies from the browser
cj = browser_cookie3.firefox()
if not ("advent" in str(cj)):
	cj = browser_cookie3.chrome()
		
#Get today number of day
day_today = date.today().strftime("%d").lstrip("0")

#If we provide an argument, use it as the desired day. Ex: ./startDay.py 5. Otherwise use day_today
if len(sys.argv) > 1:
	day = int(sys.argv[1])
	if day<0 or day>31 or day>int(day_today):
		exit("Day is not valid")
else:
	day = day_today


print(f"Initializing day {day}")

if not os.path.exists(f"day{day:03}"):
	os.mkdir(f"day{day:03}")
	os.chdir(f"day{day:03}")
	r = requests.get(f"https://adventofcode.com/2019/day/{day}/input", cookies = cj)
	with open("input.txt","w") as f:
		f.write(r.text)
	with open("day{day}.py", "w") as f:
		f.write(f"\nwith open(\"day{day:03}/input.txt\") as f:\n")