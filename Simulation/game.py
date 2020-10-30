''' 이것이 코딩테스트다 with 파이썬>구현>게임구현 '''
'''
이동을 계속 반복 수행한다. 
방문한 칸은 0 -> -1로 변경한다. 
왼쪽 회전 -> 전진 or 반복(3번 회전 or 바다일 때까지) -> 후진(뒤가 바다일 경우 멈춤)
'''
'''
해당 버전의 경우 맴 외각의 예외는 고려하지 않았다.
'''

n, m = map(int, input().split())
r, c, d = map(int, input().split())

# 맵 정보를 받아온다. 0: 육지, 1: 바다
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 1 # 시작 지점 방문
d_count = 0 # 회전한 횟수(최대3)

# 왼쪽으로 회전
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

while True:
  #d = (d + 3) % 4 # 왼쪽으로 회전
  turn_left()
  fr = r + dr[d]
  fc = c + dc[d]

  # 가보지 않은 칸이 있을 경우 전진
  if array[fr][fc] == 0: 
    r, c = fr, fc
    array[r][c] = -1 # 방문했음을 표시
    d_count = 0
    count += 1
    continue
  # 가보지 않은 칸이 업거나 바다인 경우
  else:
    d_count += 1
  # 네 방향 모두 갈 수 없는 경우
  if d_count == 3:
    br = r - dr[d]
    bc = c - dc[d]
    if array[br][bc] == 0: # 뒤로 갈 수 있으면 후진
      r, c = br, bc
      d_count = 0
    else: # 뒤쪽 방향이 바다일 경우 멈춤
      break
    d_count = 0
    
print(count)
