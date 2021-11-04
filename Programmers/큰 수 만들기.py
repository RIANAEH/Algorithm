def solution(number, k):
    # 스택 개념 활용
    stack = []
    for n in number:
        while stack and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
    return ''.join(stack[:len(number)-k])

    # 테스트케이스 10 시간초과
    # answer = ''
    # start = 0
    # for i in range(1, len(number)-k+1):
    #     big = max(number[start:k+i])
    #     answer += big
    #     start += number[start:k+i].index(big) + 1
    # return answer
