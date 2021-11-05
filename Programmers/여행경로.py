def solution(tickets):
    tickets.sort(reverse=True) # 알파벳 내림차순 정렬
    graph = {}
    for a, b in tickets:
        if a in graph:
            graph[a].append(b) # 내림차순 정렬로 인해 뒷 순서가 먼저 삽입
        else:
            graph[a] = [b]
    stack = ['ICN']
    answer = []
    while stack:
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[top].pop()) # pop으로 앞 순서를 먼저 가져올 수 있음
    answer.reverse()
    return answer

# def solution(tickets):
#     # 테스트 1,2 실패
#     graph = {}
#     for a, b in tickets:
#         if a in graph:
#             graph[a].append(b)
#         else:
#             graph[a] = [b]
#     answer = []
#     now = 'ICN'
#     answer.append(now)
#     for _ in range(len(tickets)):
#         try:
#             m = min(graph[now])
#             graph[now].remove(m)
#             now = m
#             answer.append(now)
#         except:
#             print("error")
#     return answer
