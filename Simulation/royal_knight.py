''' 이것이 코딩테스트다 with 파이썬>구현>왕실의 나이트 '''
'''
이동할 수 있는 모든 경우에 대한 검사를 수행한다. 
'''

input_data = input()
x, y = int(ord(input_data[0]) - ord('a')) + 1, int(input_data[1]) # x, y 좌표를 숫자로 변환
count = 0

# 이동할 수 있는 모든 경우 8가지
moves = [(-2, 1), (-2, 1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

# 모든 경우 확인
for mx, my in moves: # for move in moves:의 형태로 반복문을 사용할 수 있으며, 이럴 경우 move[0], move[1]로 접근 가능하다.  
  tx = x + mx
  ty = y + my
  if tx < 1 or ty <1 or tx > 8 or ty > 8:
    continue
  # 이동가능할 경우 
  count += 1

print(count)
