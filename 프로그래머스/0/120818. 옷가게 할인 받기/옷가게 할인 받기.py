def solution(price):
    answer = int(price)
    if price >= 100000:
        answer = int(price*(100-5)/100)
        if price >= 300000:
            answer = int(price*(100-10)/100)
            if price >= 500000:
                answer = int(price*(100-20)/100)
    return answer