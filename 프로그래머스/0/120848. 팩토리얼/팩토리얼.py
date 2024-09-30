def solution(n):
    answer = 0
    fac = 1
    while n>=fac:
        answer+=1
        fac = answer*fac
    return answer-1