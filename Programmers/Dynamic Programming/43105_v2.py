def solution(triangle):
    # 두가지 경로 중 큰 값으로 변경한다. 
    for i in range(1, len(triangle)):
        triangle[i][0] = triangle[i][0] + triangle[i - 1][0]
        
        for j in range(1, i):
            triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])
        
        triangle[i][i] = triangle[i][i] + triangle[i - 1][i - 1]
    
    # 최댓값을 return
    return max(triangle[-1])
