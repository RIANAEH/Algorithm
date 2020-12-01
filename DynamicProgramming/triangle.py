''' 프로그래머스>코딩테스트 연습>동적계획법>정수 삼각형(level3) '''
'''
단말 노드별로 각각의 최대값을 구하고 그 중의 최대를 찾는다. 
단말 노드에서 루트 노드까지 거꾸로 올라가면서 최대값을 찾는다. 
'''
def solution(triangle):
    answer = 0
    # 삼각형의 높이
    h = len(triangle) 
    # 다이나믹 프로그래밍 테이블(단말 노드까지의 최대값 저장)
    d = [0] * h 
    
    for i in range(h):
        sum = triangle[h - 1][i]
        for j in range(h - 2, -1, -1):
            if i - 1 < 0
    
    return answer
