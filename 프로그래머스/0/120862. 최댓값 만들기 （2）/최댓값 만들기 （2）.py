def solution(numbers):
    answer = numbers[0]*numbers[1]
    for idx,i in enumerate(numbers):
        for j in numbers[idx+1:len(numbers)]:
            if i*j>answer:
                answer = i*j
    return answer