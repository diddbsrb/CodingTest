def solution(angle):
    answer = 2 if angle==90 else 1 if 0<angle<90 else 4 if angle==180 else 3
    return answer