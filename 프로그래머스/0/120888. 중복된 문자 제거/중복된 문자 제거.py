def solution(my_string):
    lst = list(my_string)
    ans_lst = []
    for i in lst:
        if i not in ans_lst:
            ans_lst.append(i)
    return ''.join(ans_lst)