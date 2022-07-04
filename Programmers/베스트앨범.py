# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    data = []
    
    for genre in set(genres):
        temp = []
        total_play = 0
        for i in range(len(genres)):
            if genres[i] == genre:
                temp.append((i, plays[i]))
                total_play += plays[i]
        temp.sort(key = lambda x : -x[1])
        data.append((genre, temp, total_play))
    data.sort(key = lambda x : -x[2])
    
    for d in data:
        for i in range(len(d[1])):
            if i > 1:
                break
            answer.append(d[1][i][0])
    
    return answer
