""" problems: https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input().strip())
listN = list(map(int,input().strip().split()))
    
M = int(input().strip())
listM = list(map(int,input().strip().split()))
    
setM = set(listN)
setN = set(listM)
    
set3 = sorted((setM.union(setN) - (setM.intersection(setN))))

for item in set3:
    print('{}'.format(item))