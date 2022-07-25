# 백트래킹 활용
n, m = map(int, input().split())

def dfs(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i not in s:
            dfs(s + [i])

dfs([])

# 순열 활용
# from itertools import permutations

# n, m = map(int, input().split())
# numbers = [i for i in range(1, n + 1)]

# answer = list(permutations(numbers, m))
# for aa in answer:
#     for a in aa:
#         print(a, end=" ")
#     print() 
