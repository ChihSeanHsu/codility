

def solution(A, B, K):
    # write your code in Python 3.6
    answer = 1
    mod = A % K
    
    if mod != 0:
        lastest_can_mod = A + mod
    else:
        lastest_can_mod = A
    
    
    for _ in range(1, 2000000001):
        lastest_can_mod += K
        if lastest_can_mod <= B:
            answer += 1
        else:
            break
    
    return answer

