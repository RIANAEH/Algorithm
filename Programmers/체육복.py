def solution(n, lost, reserve):
    lost_ = [l for l in lost if l not in reserve]
    reserve_ = [r for r in reserve if r not in lost]
    if len(reserve_) != 0:
        reserve_.sort() # 추가 된 테스트케이스 통과 하려면..
    for r in reserve_:
        if r-1 in lost_:
            lost_.remove(r-1)
        elif r+1 in lost_:
            lost_.remove(r+1)    
    return n - len(lost_)
