'''
ID: tgac2021
LANG: PYTHON3
TASK: friday
'''

fin = open("friday.in", "r")
N = int(fin.readline().strip())
dayOfWeek = {i:0 for i in range(7)}
day = 0
months = [31, 28, 31, 30, 31, 30, 31, 31,30,31,30,31]

for year in range(1900, 1900+N):
    for month in months:
        dayOfWeek[day%7] += 1
        if(month==28):
            if(year % 4 == 0 and year % 100 != 0) or  (year % 100 == 0 and year % 400 == 0):
                day += 29
                continue
        day += month

with open('friday.out', 'w') as fout:
    for day in range(6):
        fout.write(f"{dayOfWeek[day]} ")
    fout.write(f"{dayOfWeek[6]}\n")
