def solution(num_list, n):
    answer = []
    for i in range(int(len(num_list)/n)):
        answer.append(num_list[i*n:i*n+n])
    return answer