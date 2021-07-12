# Binary Search in a Rotated Array

## Algorithm
Since the array is rotated, a regular binary search will not work as the mid element
is not necessarily the median.

It is trivial to re-order the array, however doing so would require a time complexity
of `O(n)` depending on the algorithm selected and whether the array is rotated
left by 1, or right by 1.

Hence we will go with the binary search approach with additional conditions to
decide whether to search in the left half or right half.


## Time Complexity
There are additional comparisions that we are doing to decide whether to search
in the left half or the right half. We are making at most `3` additional
comparisions to do this. These additional comparisions happen in constant time
for each iterations, hence happens in `O(1)`.

Post the comparison, we are dividing the array into 2 and searching on only 
one half of the elements in each iteration. Since we are reducing the 
problem space `n = n/2` every time, this is the same as a regular binary search.

Time complexity = `O(log(n))`.

## Space Complexity
There is no additional space required since we are searching within the original
array itself. Only the value of `mid` is stored for each iteration. Hence space
complexity is `O(1)`.
