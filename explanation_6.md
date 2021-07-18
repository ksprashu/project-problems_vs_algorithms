# Get min, max from an array in a single pass.

## Algorithm
Setting the first element as the minimum and maximum, traverse through the 
array in a single pass updating the min and max if the next element found
was smaller or larger than the already recorded value.

## Time Complexity
There are a few constant time operations to set the min and max variables. 
Other than this, we traverse through the array only once, and hence the time
complexity is `O(n)`.

## Space Complexity
Only a couple of variables are used to maintain the min and max values. The 
input array is parsed in memory. Hence the space complexity is `O(1)`
