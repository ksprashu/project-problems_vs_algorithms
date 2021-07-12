"""Program to Search in a Rotated Sorted Array.

You are given a sorted array which is rotated at some random pivot point.
Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index,
otherwise return -1.

Logic:
Finding the pivot and fixing the array will cost O(n) time.
Can we use a modified binary search?
if n > mid, then
  if n < end -> go right
  if end < mid (is rotated) -> go right
  else -> go left
if n < mid, then
  if n > beg -> go left
  if beg > mid (is rotated) -> go left
  else -> go right
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return sub_array_search(input_list, number, 0, len(input_list) - 1)


def sub_array_search(arr, target, beg, end):
    """Search between beg and end index.
    """

    # base conditon
    if beg > end:
        return -1
    
    mid = beg + (end - beg) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        if target <= arr[end] or arr[end] < arr[mid]:
            return sub_array_search(arr, target, mid + 1, end)  # go right
        else:
            return sub_array_search(arr, target, beg, mid - 1)  # go left
    elif target < arr[mid]:
        if target >= arr[beg] or arr[beg] > arr[mid]:
            return sub_array_search(arr, target, beg, mid - 1)  # go left
        else:
            return sub_array_search(arr, target, mid + 1, end)  # go right


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# unrotated sorted array
print(rotated_array_search([1, 2, 3, 4, 5, 6], 4))
# 3
print(rotated_array_search([1, 2, 3, 4, 5, 6], 1))
# 0
print(rotated_array_search([1, 2, 3, 4, 5, 6], 6))
# 5

# rotated sorted arrays
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 4))
# 8
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
# 0
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 9))
# 3
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 10))
# 4
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# 5

# number not found
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 4], 3))
# -1
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 12))
# -1
print(rotated_array_search([6, 7, 8, 10, 1, 2, 3, 4], 9))
# -1
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], -1))
# -1

# rotated edge cases, single rotations
print(rotated_array_search([4, 5, 6, 7, 8, 1, 2], 8))
# 4
print(rotated_array_search([4, 5, 6, 7, 0, 1, 2], 1))
# 5
print(rotated_array_search([7, 0, 1, 2, 3, 4, 5, 6], 7))
# 0
print(rotated_array_search([7, 0, 1, 2, 3, 4, 5, 6], 5))
# 6
print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 0], 0))
# 7
print(rotated_array_search([1, 2, 3, 4, 5, 6, 7, 0], 2))
# 1
