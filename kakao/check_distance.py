''' 2021 카카오 채용 연계형 인턴십 : 거리두기 확인하기 '''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(places):
    answer = []
    for p in places:
        answer.append(check(p))
    return answer

def check(p):
    for x in range(5):
        for y in range(5):
            if p[x][y] == "P":
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                        continue
                    if p[nx][ny] == "X":
                        continue
                    if p[nx][ny] == "P":
                        return 0
                    for i in range(4):
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                        if nnx == x and nny == y:
                            continue
                        if nnx < 0 or nny < 0 or nnx >= 5 or nny >= 5:
                            continue
                        if p[nnx][nny] == "X":
                            continue
                        if p[nnx][nny] == "P":
                            return 0
                        
    return 1
