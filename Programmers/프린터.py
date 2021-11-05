from collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque()
    for i in range(len(priorities)):
        queue.append((priorities[i], i))
    while True:
        big = max(queue)[0]
        now = queue.popleft()
        if now[0] == big:
            if now[1] == location:
                return answer
            else:
                answer += 1
        else:
            queue.append(now)
