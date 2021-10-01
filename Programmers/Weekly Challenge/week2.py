def solution(scores):
    answer = ''

    for i in range(0, len(scores)):
        score_array = []

        # 해당 학생의 점수를 모은다. 
        for j in range(0, len(scores)):
            score_array.append(scores[j][i])

        my_score = scores[i][i]
        # 최고/최저점이며
        if my_score == max(score_array) or my_score == min(score_array):
            # 유일할 경우
            if score_array.count(my_score) == 1:
                # 해당 점수 삭제
                score_array.remove(my_score)

        # 평균을 구하고 학점을 부여한다. 
        answer += checkGrade(sum(score_array) / len(score_array))

    return answer

def checkGrade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"
