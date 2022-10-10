'''
ID: tgac2021
LANG: PYTHON3
TASK: friday
'''

fin = open("friday.in", "r")
fout = open("friday.out", "w")

# 30 days: April (4), June (6), September (9), November (11)
# 31 days: January (1), March (3), May (5), July (7), 
#          August (8), October (10),
#          December (12)
# 
# February has 28, except in leap years when it has 29.
# Every year evenly divisible by 4 is a leap year 
# The rule above does not hold for century years. 
# Century years divisible by 400 are leap years, all others are not. 
# Thus, the century years 1700, 1800, 1900 and 2100 are not leap years, but 2000 is a leap year.

num_yrs = int(fin.readline().strip())
start = [1, 1, 1990] # Monday
end = [1, 1, 1990 + num_yrs - 1]

friday13 = [0 for x in range(7)]

month = start[0]
day = start[1]
year = start[2]

i = 0
while [month, day, year] != end:
    if day == 13:
        friday13[i % 7] += 1
    # Feb :)
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or  (year % 100 == 0 and year % 400 == 0):
            if day == 29:
                month += 1
                day = 1
        else:
            if day == 28:
                month += 1
                day = 1

    # 30 days
    if month in [4, 6, 9, 11]:
        if day == 30:
            month += 1
            day = 1 

    # 31 days
    if month in [1, 3, 5, 7, 8, 10]:
        if day == 31:
            month += 1
            day = 1

    # New Year!
    if month == 12:
        if day == 31:
            month, day = 1, 1
            year += 1
    
    day += 1
    i += 1

for day in friday13:
    fout.write(f"{day} ")