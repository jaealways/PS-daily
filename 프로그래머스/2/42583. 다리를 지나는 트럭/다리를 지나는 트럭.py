"""
passed, bridge, wait = [],[0,0],[]
bridgesum + wait[0] < 최대 -> wait popleft
아니면 popleft 후 (passed에 append) append(wait[0])

len(passed)==n: 종료

"""

def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer,n,bridgesum=0,len(truck_weights),0
    passed,bridge,wait=deque([]),deque([0 for _ in range(bridge_length)]),deque(truck_weights)
    
    while len(passed)<n:
        answer+=1
        p=0
        if wait:
            p=wait[0]
        e=bridge.popleft()
        if e>0:
            passed.append(e)
        bridgesum-=e
        if bridgesum+p<=weight:
            bridgesum+=p
            bridge.append(p)
            if wait:
                wait.popleft()
        else:
            bridge.append(0)
    return answer