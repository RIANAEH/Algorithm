''' 프로그래머스>코딩테스트 연습>완전탐색>모의고사(level1) '''
'''
1, 2, 3번의 답안을 리스트로 만들어야한다. -> 리스트로 모두 만들필요 없이 패턴 리스트를 순환하면 된다.
최대 10,000 문제이므로 한문제씩 모두 비교해도 30,000경우이므로 한문제씩 비교해도 된다.
'''

def solution(answers):
    answer = []
    counts = [0] * 3 # 맞힌 문제 수(초기화 필수)

    # 1, 2, 3 수포자의 패턴
    std1 = [1, 2, 3, 4, 5] # 5
    std2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    # 정답과 비교
    for i in range(len(answers)):
        if std1[i % len(std1)] == answers[i]:
            counts[0] += 1
        if std2[i % len(std2)] == answers[i]:
            counts[1] += 1
        if std3[i % len(std3)] == answers[i]:
            counts[2] += 1
            
    # 맞힌 문제수에 따라 큰 순서로 정렬
    temp = sorted(counts, reverse = True)
    
    # 가장 많이 맞힌 사람 
    for i in range(len(counts)):
        if counts[i] == temp[0]:
            answer.append(i+1) 
    
    return answer
