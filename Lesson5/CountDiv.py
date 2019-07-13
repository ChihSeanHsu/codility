def solution(A, B, K):
    # write your code in Python 3.6
    answer = 0
    try:
        mod = A % K
        
        if mod != 0:
            lastest_can_mod = A + mod
            assert lastest_can_mod < B, 'No mod'
        else:
            lastest_can_mod = A
            
        answer += 1
        gap = B - lastest_can_mod
        divisor = int(gap / K)
        answer += divisor
    except:
        pass
    
    return answer
