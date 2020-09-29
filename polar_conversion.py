""" PROBLEM STATEMENTS: https://www.hackerrank.com/challenges/polar-coordinates/problem"""

import cmath
Z = input()
print(abs(complex(Z)))
print(cmath.phase(complex(Z)))