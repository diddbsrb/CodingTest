def solution(numbers, direction):
    answer = []
    if direction == 'left':
        a = numbers.pop(0)
        answer = numbers+[a]
    else:
        a = numbers.pop(-1)
        answer = [a]+numbers
    return answer