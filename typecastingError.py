"""problem statements: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem"""
import sys


S = input().strip()
try:
    a = int(S)
    print(a)
except:
    print("Bad String")