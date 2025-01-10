def solution(cipher, code):
    lst = []
    idx = code
    while len(cipher)>idx-1:
        lst.append(cipher[idx-1])
        idx+=code
    return ''.join(lst)