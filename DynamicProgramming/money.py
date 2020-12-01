''' 이것이 코딩테스트다 with 파이썬>다이나믹 프로그래밍>효율적인 화폐 구성(level2) '''

n, m = map(int, input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001] * (m + 1) # 불가능한 수로 10001을 설정

d[0] = 0
for i in range(n):
  for j in range(array[i], m + 1):
    if d[j - array[i]] != 10001: # (i - k) 원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[m])
