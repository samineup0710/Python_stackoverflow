""" problem statement link:https://www.hackerrank.com/challenges/calendar-module/problem"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
MM, DD, YYYY = map(int, input().split())
dateX = calendar.day_name[calendar.weekday(YYYY, MM, DD)].upper()                   #.weekday gives integer from 0-6
print(dateX)

