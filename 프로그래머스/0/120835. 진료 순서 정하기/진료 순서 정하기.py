def solution(emergency):
    answer = []
    so = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(so.index(i)+1)
    return answer