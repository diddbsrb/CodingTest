def solution(array, n):
    lst = []
    for i in array:
        lst.append(abs(i-n))
    pos = []
    for idx, i in enumerate(lst):
        if i == min(lst):
            pos.append(idx)
    result = []
    for i in pos:
        result.append(array[i])
    return min(result)