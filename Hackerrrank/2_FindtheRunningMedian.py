def runningMedian(a):
    # Declaring two min heap
		# import at the top
		# from heapq import heappush, heappop, heapify
    
    g = []
    s = []
    result = []
    for i in range(len(a)):
       
        # Negation for treating it as max heap
        heappush(s, -a[i])
        heappush(g, -heappop(s))
        if len(g) > len(s):
            heappush(s, -heappop(g))
 
        if len(g) != len(s):
            result.append(float(-s[0]))
        else:
            result.append(float((g[0] - s[0])/2))
        
    return result