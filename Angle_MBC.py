""" problem statements: https://www.hackerrank.com/challenges/find-angle/problem?h_r=next-challenge&h_v=zen"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan2, degrees
AB = float(input())
BC = float(input())
hypeAC = float(AB/BC)
AM = float(hypeAC/2)
MC = AM
#trABM & trBMC are congurent by sas axiom

print(str(int(round(degrees(atan2(AB, BC)),0))) + '°')