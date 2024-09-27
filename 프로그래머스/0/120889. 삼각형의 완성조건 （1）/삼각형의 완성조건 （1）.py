def solution(sides):
    m = max(sides)
    sides.remove(m)
    if sum(sides)>m:
        answer = 1
    else:
        answer = 2
    return answer