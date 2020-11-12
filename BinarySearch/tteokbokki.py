''' 이것이 코딩테스트다 with 파이썬>이진탐색>떡볶이 떡 만들기(level2) '''
'''
절단기로 자른 떡의 길이를 모두 더한 것이 target 보다 크거나 같으면 된다. 
절단기의 길이는 약 10억가지가 가능하다. -> 이진 탐색
이진 탐색에서 중간지점을 계속해서 탐색하면서 최적화된 값을 찾아나가게된다. 
'''
def binary_search(array, target, start, end):
  answer = 0
  while start <= end:
      # 절단기의 길이
    mid = (start + end) // 2
    # 절단기로 자른 떡의 총 길이를 구한다.
    sum = 0
    for a in array:
      if a > mid:
        sum += a - mid
    # 총 길이가 target보다 작은 경우 절단기의 길이기 더 짧아야하므로 왼쪽을 확인한다. 
    if sum < target:
      end = mid - 1
    # 총 길이가 target보다 큰 경우 오른쪽을 확인한다. 
    else:
      # 최적화된 값을 찾기위해 답을 mid로 갱신해준다. 
      answer = mid
      start = mid + 1
  return answer

n, m = map(int, input().split())
array = list(map(int, input().split()))

# 절단기의 최대 길이
max_length = max(array) - 1

result = binary_search(array, m, 1, max_length)
print(result)
