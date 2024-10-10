def solution(array):
    dic = {}
    for i in list(set(array)):
        dic[f'{i}'] = array.count(i)
    if list(dic.values()).count(max(dic.values()))>1:
        return -1
    else:
        for i,j in dic.items():
            if j == max(dic.values()):
                return int(i)