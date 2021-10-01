def solution(table, languages, preference):
    # 문자열을 공백을 기준으로 분리하고, 행열을 생성한다. 
    lang_table = []
    for t in table:
        lang_table.append(list(t.split(" "))[1:])

    score = [0 for _ in range(5)]

    for k in range(len(languages)):
        for i in range(5):
            for j in range(5):
                # (언어 선호도 * 직업군 언어 점수)를 누적시킨다. 
                if languages[k] == lang_table[i][j]:
                    score[i] += preference[k] * (5 - j)

    # 총합이 가장 높은 직업군 return
    position = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
    m = max(score)
    max_list = []
    for i in range(5):
        if score[i] == m:
            max_list.append(position[i])
    return min(max_list)
