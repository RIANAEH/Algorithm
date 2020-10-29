'''프로그래머스>코딩테스트연습>Greedy>조이스틱(level2)'''
'''
조이스틱의 왼쪽, 오른쪽 이동의 최소화가 핵심
보통의 경우 좌우 이동의 수 : name길이 - 1 -> A가 존재할 경우 달라진다.
시작할 때 오른쪽, 왼쪽 중 A가 아닌 알파벳이 가까이 있는 방향으로 이동을 시작해서
가장 멀리 있는 A가 아닌 알파벳까지 이동해야한다.
같은 원리도 조이스틱의 위, 아래 이동의 최소화 또한 고려해 줘야한다. 

print(solution(BBBAAAB))#9
print(solution(ABABAAAAABA)) #11
위와 같은 경우 이동 중에 방향을 바꿔야한다. 
따라서 이동 하나하나 당 다음 이동에 대한 좌우 비교를 통해 이동 방향을 수시로 결정해야한다. 
'''
def solution(name):
    answer = 0
    i = 0
    not_a = []
    
    for value in name:
        if value != 'A':
            dif = ord(value) - ord('A')
            answer += min(dif, 26 - dif) # 위, 아래 중 최소 방향으로 이동
            if i != 0:
                not_a.append(i)
        i += 1
    
    len_not_a = len(not_a)
    cursor = 0
    if len_not_a != 0: # 모두 A일 경우, name의 길이가 1일 경우는 좌우로 이동하지 않음
        for _ in range(len_not_a):            
            right = 0
            left = 0
            if cursor < not_a[0]:
                right = abs(not_a[0] - cursor)
            else:
                right = len(name) - abs(not_a[0] - cursor)
            if cursor < not_a[-1]:
                left = len(name) - abs(not_a[-1] - cursor)
            else:
                left = abs(not_a[-1] - cursor)
            if left >= right: # 오른쪽으로 이동
                answer += right
                cursor = not_a[0]
                del not_a[0]
            else:
                answer += left
                cursor = not_a[-1]
                del not_a[-1]
    
    return answer
