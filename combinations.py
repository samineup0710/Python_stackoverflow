from itertools import combinations
S, r = input().split()   #for multiple inputs. here two only
for i in range(1, int(r)+1):
    comb = ["".join(sorted(i)) for i in combinations(str(S), int(i))]
    comb.sort()
    print("\n".join(comb)) 
