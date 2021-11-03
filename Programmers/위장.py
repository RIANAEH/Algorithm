from collections import Counter

def solution(clothes):
    answer = 1
    for n in Counter([cat for name, cat in clothes]).values():
        answer *= n+1
    return answer - 1
    # answer = 1
    # cat_list = []
    # for clothe in clothes:
    #     cat_list.append(clothe[1])
    # for n in Counter(cat_list).values():
    #     answer *= n+1
    # return answer - 1
