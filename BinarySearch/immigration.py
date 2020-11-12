''' 코딩테스트 연습>이분탐색>입국심사'''
'''
걸릴 수 있는 최대시간이 약 10억 X 10억 으로 굉장히 그 값이 크다.
그 중 우리는 최적의 시간을 찾으면 되기 때문에 이진 탐색을 이용한다. 
계속해서 최적의 시간을 탐색하면서 그 시간에 심사 가능한 사람의 수를 구해 원하는 n명의 사람에 부합하는 지 검사한다. 
'''
def solution(n, times):
    answer = 0
    start = 0
    end = n * max(times) # 걸릴 수 있는 최대시간
    
    while start <= end:
        mid = (start + end) // 2 
        # mid의 시간 동안 심사받을 수 있는 사람의 수를 구한다. 
        people = 0
        for t in times:
            people += mid // t
        # 요구하는 사람 수보다 적을 경우 시간을 늘려서 다시 검사
        if people < n:
            start = mid + 1
        # 요구하는 사람 수보다 같거나 많을 경우 시간을 줄여서 다시 검사
        else:
            # 최적 시간 갱신
            answer = mid
            end = mid - 1
            
    return answer
