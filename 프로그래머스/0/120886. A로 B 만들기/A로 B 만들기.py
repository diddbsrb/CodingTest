def solution(before, after):
    dic_before = {}
    dic_after = {}
    for i in before:
        if i in dic_before:
            dic_before[i]+=1
        else:
            dic_before[i]=1
    for i in after:
        if i in dic_after:
            dic_after[i]+=1
        else:
            dic_after[i]=1
    return 1 if dic_before==dic_after else 0