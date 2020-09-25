# Enter your code here. Read input from STDIN. Print output to STDOUT
import os
from itertools import product
a= input()
b = input()
A = map(int, a.split())
B = map(int, b.split())
products = product(A,B)
print(*products)
