""" problem statements: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem """

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = map(int, input().split(' '))
#input1 = ['a', 'a', 'b', 'a', 'b']
#input2 = ['a', 'b']
input1 = list()
for i in range(n):
    input1.append(input())
    input2 = list()
for i in range(m):
    input2.append(input())
dic = defaultdict(list)
for i in range(n):
    dic[input1[i]].append(i+1)
for i in input2:    
    if i in dic:
        print(*dic[i])
    else:
        print(-1)