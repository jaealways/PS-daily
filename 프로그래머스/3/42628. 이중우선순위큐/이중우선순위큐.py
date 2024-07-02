"""
최대값, 최소값의 pop 값 다름 -> 지워도 됨
같거나, 비어있음 -> 지우면 안됨

heapq.nlargest(heap,x)


"""

def solution(operations):
    import heapq
    
    answer,heap = [0,0],[]
    heapq.heapify(heap)
    for op in operations:
        print(op,heap)
        od,n=op.split()
        if od=='I':
            heapq.heappush(heap,int(n))
            continue
        if not len(heap):
            continue
        if n=='1':
            heap.pop()
        else:
            heapq.heappop(heap)
    if heap:
        answer=[max(heap),min(heap)]
    return answer