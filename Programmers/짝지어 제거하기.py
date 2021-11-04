def solution(s):
    # 문제 조건 좀 잘 읽자!!
    stack = []
    for n in s:
        if stack and stack[-1] == n:
            temp = stack.pop()
        else: 
            stack.append(n)
    return 1 if not stack else 0
