''' 이것이 코딩테스트다 with 파이썬>이진탐색>부품 찾기(level1.5) '''
'''
최대 N X M, 즉 100,000,000,000 개의 데이터가 입력될 수 있다. 이는 엄청 많은 데이터이므로 이진탐색을 고려해볼 수 있다.
이진 탐색을 이용할 경우 N개의 데이터에 대해 정렬을 수행해야하므로 O(N X logN)의 시간 복잡도가 요구되며, 후에 M개의 데이터에 대한 검사에는 이진 탐색이 사용되어 O(M X logN)의 시간 복잡도가 요구된다. 
따라서, 시간 복잡도는 O((N + M) X logN)이 된다. 

1. 먼저 매장 내 N개의 부품을 번호를 기준으로 정렬한다. 
2. 그 이후 M개의 찾고자 하는 부품이 각각 매장에 존재하는지 이진 탐색으로 검사한다. 
'''
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

n = int(input())
n_list = list(map(int, input().split()))
# 이진 탐색을 수행하기 위해 사전에 정렬 수행
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

for mv in m_list:
  result = binary_search(n_list, mv, 0, n - 1)
  if result == None:
    print("no", end=" ")
  else:
    print("yes", end=" ")
