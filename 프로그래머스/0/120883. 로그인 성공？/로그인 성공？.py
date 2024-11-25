def solution(id_pw, db):
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in [x[0] for x in db]:
        answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer