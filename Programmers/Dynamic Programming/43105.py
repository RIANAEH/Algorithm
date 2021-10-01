def solution(triangle):
    # dp 테이블을 생성한다. 
    dp = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        dp.append([0 for _ in range(i + 1)])

    # 경로를 탐색하며 더 큰 합으로 변경한다. 
    for i in range(len(triangle) - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    # 최댓값을 return
    return max(dp[len(triangle) - 1])
