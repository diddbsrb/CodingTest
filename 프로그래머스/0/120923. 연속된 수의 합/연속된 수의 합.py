def solution(num, total):
    num1 = (total-sum([i for i in range(1,num+1)]))/num
    return [i for i in range(int(num1+1),int(num1+num+1))]