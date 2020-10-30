''' 프로그래머스>코딩테스트 연습>완전탐색>모의고사(level1) '''
'''
1, 2, 3번의 답안을 리스트로 만들어야한다. -> 리스트로 모두 만들필요 없이 패턴 리스트를 순환하면 된다.
최대 10,000 문제이므로 한문제씩 모두 비교해도 30,000경우이므로 한문제씩 비교해도 된다.

'''

def solution(answers):
    answer = []
    counts = [] # 맞힌 문제 수

    # 1, 2, 3 수포자의 패턴
    std1 = [1, 2, 3, 4, 5] # 5
    std2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    # 정답과 비교
    for i in range(n):
        if std1[i % 5] == answers[i]:
            counts[0] += 1
        if std2[i % 8] == answers[i]:
            counts[1] += 1
        if std3[i % 10] == answers[i]:
            counts[2] += 1
            
    # 맞힌 문제수에 따라 큰 순서로 정렬
    temp = sorted(counts, reverse = True)
    
    for t in temp:
        if t == counts[0]:
            answer.append()
    ans1, ans2, ans3 = [], [], [] 
    p1 = [1, 2, 3, 4, 5]
    p3 = [3, 1, 2, 4, 5]
    for i in range(n):
        ans1.append(p1[i % 5])
        ans3.append(p3[int(i / 2) % 5]) # list indices must be integers or slices, not float
        if i % 2 == 0:
            ans2.append(p1[int(i / 2) % 5])
        else:
            ans2.append(2)
            
    # 정답과 비교
    for i in range(n):
        if ans1[i] == answers[i]:
            count[1] += 1
        if ans2[i] == answers[i]:
            count[2] += 1
        if ans3[i] == answers[i]:
            count[3] += 1
    
    # 맞힌 문제수에 따라 큰 순서로 정렬
    res = sorted(count.items(), key = lambda x: x[1], reverse = True)
    
    answer.append(res[0][0])
    if res[0][1] == res[1][1]:
        answer.append(res[1][0])
        if res[0][1] == res[2][1]:
            answer.append(res[2][0])
    
    # return 값을 오름차순으로 정렬
    answer.sort()    
    
    return answer
