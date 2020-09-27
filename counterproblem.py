"""https://www.hackerrank.com/challenges/collections-counter/problem"""
from collections import Counter

X = int(input())
shoes_sizes_list = list(map(int, input().split()))
print(shoes_sizes_list)
c = 0
stock = Counter(shoes_sizes_list)
print(stock)
N = int(input())                            #no of customers
for i in range(N):
    shoe_size, money  = list(map(int, input().split()))
    print(shoe_size, money)
    if stock[shoe_size]:
        c +=money
        stock[shoe_size]-=1
print(c)
    