# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
c = calendar.weekday(year, month, day)

day_names = list(calendar.day_name)
print(day_names[c].upper())