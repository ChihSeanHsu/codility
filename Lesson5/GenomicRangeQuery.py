# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# each latest position
# cauze maximum is 100000
position = {
    'A': 100001,
    'C': 100001,
    'G': 100001,
    'T': 100001
}


def solution(S, P, Q):
    
    '''
    e.g.
      S = 'ACGGTCA'
      position_mapping = {
        'A': [0, 6, 6, 6, 6, 6, 6],
        'C': [1, 1, 5, 5, 5, 5, 1000001],
        'G': [2, 2, 2, 3, 1000001, 1000001, 1000001]
      }
    '''
    length = len(S)
    position_mapping = { key: ([0] * length) for key in position.keys() }
    
   
    for idx in range(length - 1, -1, -1):
        position[S[idx]] = idx
        position_mapping['A'][idx] = position['A']
        position_mapping['C'][idx] = position['C']
        position_mapping['G'][idx] = position['G']
        position_mapping['T'][idx] = position['T']
    
    answer = [0] * len(P)
    for idx, (p, q) in enumerate(zip(P, Q)):
        if position_mapping['A'][p] <= q:
            answer[idx] = 1
        elif position_mapping['C'][p] <= q:
            answer[idx] = 2
        elif position_mapping['G'][p] <= q:
            answer[idx] = 3
        else:
            answer[idx] = 4
    
    return answer

