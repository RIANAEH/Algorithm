from sys import stdin
from collections import Counter

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))

counter = Counter(cards)
for target in targets:
    print(counter[target], end=" ")
    