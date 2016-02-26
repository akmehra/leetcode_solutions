#for min heap, use inbuilt library heapq
#for max heap, invert all elements and use min heap
import heapq
#incoming stream of numbers till user prints end

input = int(raw_input("Please enter the damn number : Heaps are useful but they irritate"))
min_heap = []
max_heap = []



while input != 0:
    current_average = 0

    heapq.heappush(min_heap, (input))
    heapq.heappush(max_heap, -(input))

    current_average = ( (min_heap[0]) - ((max_heap[0])) )/2
    print "Current average is " + str(current_average)
    input = int(raw_input("Please enter the damn number : Heaps are useful but they irritate"))

#testing heapify function

n = [6,5,4,3,2,1]
heapq.heapify(n)

print n
