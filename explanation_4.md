# Sort an array with only 0, 1, 2 in a single pass.

## Algorithm
We need to sort this data in just one traversal pass. 
The way this can be done is by moving any 0's to the beginning and moving
any 2's to the end. The 1's will automatically be left in the middle.

## Traversal
There are two bookmark pointers `beg` and `end` that will hold the last
position of 0's and the first position of 2's. Any 0's or 2's found will be
swapped to `beg` and `end` position.

A single pointer will increment through the length of the array and check for
the value. Using this, we will 'visit' each element in the array only once and 
hence we are sorting the array in a single traversal.

## Time Complexity
We do one traversal to read all the elements, this takes `O(n)` time.
In the worst case, we have to swap every element with another. This takes
`O(n)` time. Additionally a few pointers are incremented which happens in 
`O(n)` time at worst.

Total time complexity for all the operations = `O(n)`

## Space Complexity
The array is being sorted in-place. Additionally we will use a few variables 
as pointers. This is constant and hence space complexity is `O(1)` other than
the initial array.
