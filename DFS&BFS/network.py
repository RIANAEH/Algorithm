''' 프로그래머스>코딩테스트 연습>깊이/너비 우선 탐색(DFS/BFS)>네트워크 '''
''' 
DFS, 얼음 문제와 비슷
행을 돌아가면서 방문한적이 있는 행일 경우 넘어가고 방문한적 없는 행일 경우 새로운 네트워크를 추가하고 탐색을 시작한다. 
탐색을 하는 과정에서 연결되어있는 노드를 발견할 경우 해당 노드에 방문 표시를 하고 해당 노드의 행으로 넘어가 탐색을 시작한다. (for문으로 처음 탐색을 시작한 행의 모든 열을 검사한다.)
'''
def solution(n, computers):
    network = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            # 방문하지 않은 노드일 경우 네트워크+1, 탐색 시작
            network += 1
            dfs(i, n, computers, visited)
    return network

def dfs(x, n, computers, visited):
    # 방문 표시
    visited[x] = True
    # 행의 모든 열을 검사
    for i in range(n):
        # 연결되어있고, 방문한적 없으면 탐색(재귀)
        if computers[x][i] == 1 and not visited[i]:
            dfs(i, n, computers, visited)
