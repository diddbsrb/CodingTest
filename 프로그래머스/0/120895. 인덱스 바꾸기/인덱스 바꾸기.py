def solution(my_string, num1, num2):
    lst = list(my_string)
    str1 = lst[num1]
    str2 = lst[num2]
    lst[num1] = str2
    lst[num2] = str1
    return ''.join(lst)