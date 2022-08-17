from sys import stdin

n = int(stdin.readline())
sequence = list(map(int, stdin.readline().split()))

answer = [0] * n
answer[0] = 1
for i in range(1, len(sequence)):
    tmp = list()
    for j in range(i - 1, -1, -1):
        if sequence[i] > sequence[j]:
            tmp.append(answer[j])
    answer[i] = max(tmp) + 1 if tmp else 1
print(max(answer))
    