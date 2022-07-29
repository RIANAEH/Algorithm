from sys import stdin
from itertools import combinations

while(True):
    data = list(map(int, stdin.readline().split()))
    if data[0] == 0:
        break
    for l in list(combinations(data[1:], 6)):
        print(*l)
    print()
