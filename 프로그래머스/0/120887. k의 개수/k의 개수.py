def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        for a in str(num):
            if a == str(k):
                answer+=1
    return answer