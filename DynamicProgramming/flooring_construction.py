''' 이것이 코딩테스트다 with 파이썬>다이나믹 프로그래밍>바닥 공사(level1.5) '''

n = int(input())

d = [0] * 1001 
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
  d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])
