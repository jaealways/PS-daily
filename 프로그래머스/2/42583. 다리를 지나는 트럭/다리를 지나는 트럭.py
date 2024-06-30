"""
truck_weight popleft -> bridge popleft -> after_bridge
n=len(truck_weight)

popleft -> next truck()
if next_truck not -1:
    popleft 하지말기
if next_truck + bridge < weight:
    next_truck=-1


if after_bridge==n이면 stop
    
"""

def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    truck_weights=deque(truck_weights)
    answer,n,next_truck,bridge_sum=0,len(truck_weights),0,0
    after_bridge,bridge=[],deque([0 for _ in range(bridge_length)])
    
    while len(after_bridge)<n:
        if next_truck==0 and len(truck_weights):
            next_truck=truck_weights.popleft()
        t=bridge.popleft()
        bridge_sum-=t
        if t>0:
            after_bridge.append(t)
        if next_truck+bridge_sum<=weight:
            bridge_sum+=next_truck
            bridge.append(next_truck)
            next_truck=0
        else:
            bridge.append(0)
        answer+=1
    
    return answer