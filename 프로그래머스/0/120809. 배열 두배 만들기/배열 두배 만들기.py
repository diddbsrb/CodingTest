def solution(numbers):
    answer = numbers
    for i, j in enumerate(numbers):
        answer[i] = j*2
    return answer