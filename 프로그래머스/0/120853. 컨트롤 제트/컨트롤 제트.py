def solution(s):
    lst = s.split(' ')
    answer = 0
    for idx, i in enumerate(lst):
        try:
            answer+=int(i)
        except:
            answer-=int(lst[idx-1])
    return answer