''' 이것이 코딩테스트다 with 파이썬>구현>시간 '''
'''
하루는 86,400초로 모든 경우의 수가 1000,000 보다 작아 하나하나 확인해볼 수 있다. 
'''

h = int(input())

count = 0
for i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
