def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
    # for person in participant:
    #     if person in completion:
    #         completion.remove(person)
    #     else:
    #         return person
