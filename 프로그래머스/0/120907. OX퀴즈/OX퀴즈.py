def solution(quiz):
    answer = []
    for i in quiz:
        lst = i.split(' ')
        if lst[1] == '+':
            if int(lst[0])+int(lst[2]) == int(lst[4]):
                answer.append('O')
            else:
                answer.append('X')
        if lst[1] == '-':
            if int(lst[0])-int(lst[2]) == int(lst[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer