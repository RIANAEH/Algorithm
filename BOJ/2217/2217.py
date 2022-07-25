n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()

answer = 0
for i in range(n):
    answer = max(answer, ropes[i] * (n - i))

print(answer)
