# Rearrange array elements to find 2 numbers with maximum sum

## Algorithm
In order to find two numbers such that the sums are the largest, the two
numbers have to be built such that the digits are selected from a 
sorted array.

In order to do this, we will first have to sort the array.
Then we can select the elements in descending order.

I have decided to use max heap for this, since the runtime for sorting is 
just in time, as and when I select the next maximum element.

## Time Complexity

The first step is to put the elments of the array in a max heap.
Firstly, we have to traverse through all the elements of the array to build the heap.
This takes `O(n)` time.
In order to ensure that the max heap property is satisfied, we have to do a 
heapify operation. This takes `O(h)` time which is `O(log(n))` for a balanced tree.

Total time taken to fully construct the max heap is `O(n) + O(log(n)) = O(n.log(n))`

The next step is to pop the max element in order until we build the two numbers. 
To pop the max element we swap it with the last element each time. Swapping is a 
`O(1)` operation.

Re-heapifying the tree takes `O(log(n))` time.

This is done `n` time since we have to fetch all the n elements.

Total time taken is `n.O(1) + n.O(log(n))`. Ignoring lower order terms, the 
time complexity is `O(n.log(n))`.

## Space Complexity

The max heap is built in-place in the same input array. Hence no additional space
is needed. Memory is used to build the two numbers and store the index, which 
requires constant space.

Hence space complexity is `O(1)`
