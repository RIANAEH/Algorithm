def solution(people, limit):
    # 2명이 제한임을 잘 보자
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while(i <= j):
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer
