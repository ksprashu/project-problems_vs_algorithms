"""Sort an array with only 0, 1, 2 in a single pass.

Given an input array consisting on only 0, 1, and 2, 
sort the array in a single traversal. You're not allowed to use any sorting 
function that Python provides.
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Initial two pointers to beginning and end
    # Start another pointer to traverse
    # if list[curr] == 0, then beg++, travel++
    # if list[curr] == 2, then swap with end, and end--, curr++
    # if list[curr] == 1, curr++
    
    # if list[end] == 2, then end-- (to optimize swaps)
      
    beg = curr = 0
    end = len(input_list) - 1
    while curr <= end:
        if input_list[curr] == 0:
            input_list[curr], input_list[beg] = \
                input_list[beg], input_list[curr]
            beg += 1
            curr += 1
        elif input_list[curr] == 2:
            input_list[curr], input_list[end] = \
                input_list[end], input_list[curr]
            end -= 1
        elif input_list[curr] == 1:
            curr += 1
            
    return input_list


# Empty and single elements
print(sort_012([]))
# []
print(sort_012([0]))
# [0]
print(sort_012([1]))
# [1]
print(sort_012([2]))
# [2]

# already sorted
print(sort_012([0, 1]))
# [0, 1]
print(sort_012([0, 1, 2]))
# [0, 1, 2]
print(sort_012([0, 2]))
# [0, 2]
print(sort_012([1, 2]))
# [1, 2]
print(sort_012([0, 0, 1, 1, 2, 2]))
# [0, 0, 1, 1, 2, 2]

# permutations
print(sort_012([0, 2, 1]))
# [0, 1, 2]
print(sort_012([1, 2, 0]))
# [0, 1, 2]
print(sort_012([1, 0, 2]))
# [0, 1, 2]
print(sort_012([2, 0, 1]))
# [0, 1, 2]
print(sort_012([2, 1, 0]))
# [0, 1, 2]

# large inputs
print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, \
    2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, \
#   2, 2, 2, 2, 2, 2, 2, 2, 2]    
print(sort_012([2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]))
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
