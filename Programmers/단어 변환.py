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

    answer = bfs(words, m, target)
        
    return answer

# 문자열을 비교하여 한개만 다를 경우 True
def compare(str1, str2):
    dif = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            dif +=1
    return True if dif == 1 else False

def bfs(words, m, target):
    q = deque()
    for i in range(len(words)):
        if m[0][i] == 1:
            # target과 같을 경우 return
            if words[i] == target:
                return m[0][i]
            # 아닐 경우 큐에 넣기
            q.append((0, i)) 
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
