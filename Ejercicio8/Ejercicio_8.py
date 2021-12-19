#Ejercicio 8

#8. You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). 
#The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.¶
#You are also given an integer array queries. The answer to the  𝑗𝑡ℎ  query is the size of the smallest interval  𝑖  such that lefti <= queries[j] <= righti.
# If no such interval exists, the answer is  −1 .

#Return an array containing the answers to the queries

import heapq

def minInterval(self, intervals, queries):
    intervals.sort()
    x = len(intervals)
    n = []
    resultado = {}
    count = 0
    for i in sorted(queries):
        while count<x and intervals[count][0] <= i:
            j, k = intervals[count]
            count = count+1
            if k >= i:
                heapq.heappush(n, [k - j + 1, k])
        while n and n[0][1] < i:
            heapq.heappop(n)
        resultado[i] = n[0][0] if n else -1
    return print([resultado[i] for i in queries])

