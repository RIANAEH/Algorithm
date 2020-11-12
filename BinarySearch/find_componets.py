''' 이것이 코딩테스트다 with 파이썬>이진탐색>부품 찾기(level1.5) '''
'''
집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때 매우 효과적이다. 
'''
n = int(input())
n_set = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for v in m_list:
  if v in n_set:
    print("yes", end=" ")
  else:
    print("no", end=" ")
