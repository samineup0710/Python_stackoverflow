""" PROBLEM STATEMENT LINK: https://www.hackerrank.com/challenges/itertools-permutations/problem """
from itertools import permutations
S, r = input().split()   #for multiple inputs. here two only
permut = ["".join(i) for i in permutations(S,int(r))]
permut.sort()
print("\n".join(permut))