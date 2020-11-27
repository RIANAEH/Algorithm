''' 이것이 코딩테스트다 with 파이썬>다이나믹 프로그래밍>개미 전사(level2)'''

n = int(input())
g = list(map(int, input().split())) # granary

# 초기값
d = [0] * 101
d[1] = g[0]
d[2] = g[1]
d[3] = g[2] + d[0]

for i in range(4, n + 1):
  # 점화식
  d[i] = g[i - 1] + max(d[i - 2], d[i - 3])

print(max(d[n], d[n - 1]))
