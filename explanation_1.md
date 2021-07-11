# Square root of an integer

## Algorithm
The identity we can use is
`sum of the first n odd number = n^2`

Hence we can keep adding the odd numbers till be reach the desired target.
The number of odd numbers that we have added will be the `floor(sqrt(n))`

## Time Complexity

Let us look at how many numbers are added to get to a given sum
|first n odd numbers| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | ... | 16 |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
| sum | 1 | 4 | 9 | 16 | 25 | 36 | 49 | 64 | 81 | 100 | 121 | 144 | ... | 256 |
|number of iterations| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | ... | 16
|(max) number of iterations| ... | 2^1 | ... | 2^2 | ... | ... | ... | 2^3 | ... | ... | ... | ... | ... | 2^4 |

By induction, for a given number `n`, we do maximum of `log(n)` iterations to get to the sum.\
eg: \
`8; log(8) = 3`\
`256; log(256) = 16`

Hence time complexity = `O(log(n))`

## Space Complexity

We store 3 values - `num`, `total`, `count` irrespective of the number of iterations
that are performed. Hence space complexity is constant = `O(1)`
