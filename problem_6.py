"""Look for smallest and largest integer from a list of unsorted integers. 

The code should run in O(n) time. 
Do not use Python's inbuilt functions to find min and max.
"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return (None, None)

    smallest = ints[0]
    largest = ints[0]

    for i in ints:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i

    return (smallest, largest)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# No elements
print(get_min_max(None))
# (None, None)
print(get_min_max([]))
# (None, None)

# Single element
print(get_min_max([0]))
# ((0, 0)
print(get_min_max([6]))
# ((6, 6)

# Same numbers
print(get_min_max([1, 1]))
# ((1, 1)
print(get_min_max([4, 4, 4]))
# ((4, 4)
print(get_min_max([99, 99, 99, 99, 99, 99]))
# ((99, 99)

# Negative numbers
print(get_min_max([-1, -4, -7, -2, -5]))
# (-7, -1)

# Other test cases
print(get_min_max([-1, 5, 2, -6, 10, 4]))
# (-6, 10)
print(get_min_max([4, 12, 7, 3, 8, 1901, 0]))
# (0, 1901)
