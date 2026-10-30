# Build max heap
def build_max_heap(processes):
    heap = [] 
    for process, priority in processes: 
        heap.append((process, priority)) 
        i = len(heap)- 1
        while i > 0: 
            parent = (i- 1) // 2 
            if heap[i][1] > heap[parent][1]: 
                heap[i], heap[parent] = heap[parent], heap[i] 
                i = parent 
            else: 
                break 
    return heap

# Execution Sequence
def execution_sequence(heap): 
    heap = heap.copy() 
    sequence = [] 
    while heap: 
        sequence.append(heap[0][0]) 
        heap[0] = heap[-1]
        heap.pop()
        n = len(heap) 
        i = 0 
        while True: 
            left = 2 * i + 1 
            right = 2 * i + 2 
            largest = i 
            if left < n and heap[left][1] > heap[largest][1]: 
                largest = left 
                
            if right < n and heap[right][1] > heap[largest][1]: 
                largest = right 
            if largest == i: 
                break 
            heap[i], heap[largest] = heap[largest], heap[i] 
            i = largest
    return sequence

# Main function
order = ["A", "B", "E", "G", "I", "H", "D", "C", "F"] 
processes = [(p, ord(p)- ord("A") + 1) for p in order] 
heap = build_max_heap(processes) 
print("Max heap array :", [p for p, _ in heap]) 
print("Execution order:", execution_sequence(heap))
