import math 

def solution(progresses, speeds):
    answer = [0]
    
    # 각 기능의 개발속도에 따른 소요 일수를 구한다. 
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 각 배포마다 몇 개의 기능이 배포되는지 retrun
    now = days[0]
    for d in days:
        if d <= now:
            answer[-1] += 1
        else:
            answer.append(1)
            now = d

    return answer
