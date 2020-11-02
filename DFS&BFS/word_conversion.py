''' 프로그래머스>코딩테스트연습>깊이/너비 우선 탐색(DFS/BFS)>단어 변환(level3)'''
'''
BFS, 최단거리 누적 -> 미로 탈출 문제와 비슷
1. 한 번에 한 개의 알파벳만 바꿀 수 있다.
2. words에 target이 없으면 0을 return 
3. 최단거리! -> 이동할 때 마다 해당 노드에 최단거리를 누적시킨다.
'''
from collections import deque

def solution(begin, target, words):
    answer = 0
    
    # 연결 matrix 만들기
    m = [[0] * len(words) for _ in range(len(words) + 1)]
    # begin 행
    for i in range(len(words)):
        if compare(begin, words[i]):
            m[0][i] = 1
    # words의 행
    for i in range(len(words)):
        for j in range(len(words)):
            if compare(words[i], words[j]):
                m[i + 1][j] = 1
    print(m)
    answer = bfs(words, m, target)
    print(m)
        
    return answer

# 문자열을 비교하여 한개만 다를 경우 True
def compare(str1, str2):
    dif = 0
    # 같은 경우 
    if str1 == str2:
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dif += 1
            # 다른 문자가 2개 이상일 경우
            if dif > 1:
                return False
    # 다른 문자가 1개인 경우
    return True

def bfs(words, m, target):
    q = deque()
    # 첫행 먼저 큐에 넣고 시작
    for i in range(len(words)):
        if m[0][i] == 1:
            # target과 같을 경우 return
            if words[i] == target:
                return m[0][i]
            # 아닐 경우 큐에 넣기
            q.append((0, i))
    # 반복해서 큐 검사
    while q:
        x, y = q.popleft()
        # pop 된 문자의 행을 모두 검사
        for i in range(len(words)):
            nx = y + 1
            # 연결되어 있을 경우 거리 1을 추가
            if m[nx][i] == 1:
                m[nx][i] = m[x][y] + 1
                # target과 같을 경우 return
                if words[i] == target:
                    return m[nx][i]
                # 아닐 경우 큐에 넣기
                q.append((nx, i))
    # target이 없을 경우
    return 0
