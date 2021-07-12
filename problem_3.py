"""Rearrange array elemnts.

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements 
are in the range [0, 9]. The number of digits in both the numbers cannot 
differ by more than 1. You're not allowed to use any sorting function that 
Python provides and the expected time complexity is O(nlog(n)).

Logic:
Condition is that number of digits cannot differ by more than 1
Hence we have to equally divide the array.
Build two numbers by taking a number each sequentially from the sorted array.

To get the sorted array, we'll use a max heap and pop from the heap.
"""

def heapify(arr, length, ix):
    """Heapify the array from the provided index.

    Args:
        arr: The list of elements
        length: The length up to which to heapify
        ix: The starting element to heapify from
    """

    left = ix * 2 + 1
    right = ix * 2 + 2

    largest_ix = ix
    if left < length and arr[left] > arr[ix]:
        largest_ix = left
    if right < length and arr[right] > arr[largest_ix]:
        largest_ix = right

    if largest_ix != ix:
        arr[ix], arr[largest_ix] = arr[largest_ix], arr[ix]
        heapify(arr, length, largest_ix)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their 
    sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    assert input_list and len(input_list) >= 2, 'Need at least 2 elements in the array'

    # build a max heap, in place
    for i in range(len(input_list) - 1, -1, -1):
        heapify(input_list, len(input_list), i)

    num1 = 0
    num2 = 0
    ix = 0
    is_num1 = True  # use this to decide which number to build
    # pop max element and build the numbers
    while ix < len(input_list):
        # build the number
        num = input_list[0]
        if is_num1:
            num1 = num1 * 10 + num
        else:
            num2 = num2 * 10 + num

        # heapify the max heap
        last_ix = len(input_list) - ix - 1
        input_list[0], input_list[last_ix] = \
            input_list[last_ix], input_list[0]
        heapify(input_list, last_ix, 0)

        # next iteration
        ix += 1
        is_num1 = not is_num1

    return [num1, num2]

# sample test cases
print(rearrange_digits([1, 2, 3, 4, 5]))
# [531, 42]
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# [964, 852]

# cannot have less than 2 digits
try:
    rearrange_digits(None)
except AssertionError as e:
    print(e)

try:
    rearrange_digits([])
except AssertionError as e:
    print(e)

try:
    rearrange_digits([1])
except AssertionError as e:
    print(e)

# two digits
print(rearrange_digits([1, 2]))
# [2, 1]
print(rearrange_digits([1, 9]))
# [9, 1]
print(rearrange_digits([5, 0]))
# [5, 0]

# three digits
print(rearrange_digits([1, 2, 0]))
# [20, 1]
print(rearrange_digits([9, 0, 6]))
# [90, 6]
print(rearrange_digits([8, 7, 6]))
# [86, 7]

# even length
print(rearrange_digits([5, 2, 7, 4]))
# [74, 52]
print(rearrange_digits([5, 2, 3, 7, 9, 1, 0, 6]))
# [9631, 7520]

# odd length
print(rearrange_digits([4, 3, 1, 8, 7]))
# [841, 73]
print(rearrange_digits([3, 5, 7, 9, 1, 2, 6, 8, 4]))
# [97531, 8642]

# def test_function(test_case):
#     output = rearrange_digits(test_case[0])
#     solution = test_case[1]
#     if sum(output) == sum(solution):
#         print("Pass")
#     else:
#         print("Fail")

# test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]