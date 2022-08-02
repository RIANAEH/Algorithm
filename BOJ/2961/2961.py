from sys import stdin
from itertools import combinations

n = int(stdin.readline())
ingredients = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

answer = 1000000000
for r in range(1, len(ingredients) + 1):
    for combs in combinations(ingredients, r):
        s = 1
        b = 0
        for c in combs:
            s *= c[0]
            b += c[1]
        answer = min(answer, abs(s - b))
print(answer)
