"""Find the square root of the integer without using any Python library.

Returns the floor value of the square root.

Logic:
Sum of first n odd numbers = n^2
n=3: 1+3+5 = 9
n=5: 1+3+5+7+9 = 25

Let us iteratively add the odd numbers till the sum is >= the target
The number of odd numbers we have added is the (floor of) sqrt
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None  # can't handle complex numbers
    # if number == 0:
    #     return number  # base condition
    
    num = 1
    total = 0
    count = 0

    while total < number:
        count += 1
        num += 2
        total += num

    return count


# Test base conditions
print(sqrt(0))
# 0
print(sqrt(1))
# 1

# Test perfect squares
print(sqrt(4))
# 2
print(sqrt(9))
# 3
print(sqrt(16))
# 4
print(sqrt(25))
# 5
print(sqrt(100)) 
# 10

print(sqrt(27))
# 5
print(sqrt(120))
# 10
print(sqrt(399))
# 19
print(sqrt(401))
# 20
