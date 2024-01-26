"""
Exponential Calculation
"""
def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * recursive_power(base, exponent - 1)

# Iterative Implementation

def iterative_power(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result


# Comparison

base_number = 2
exponent_value = 3

# Recursive
result_recursive = recursive_power(base_number, exponent_value)

# Iterative
result_iterative = iterative_power(base_number, exponent_value)

print(f"Recursive Power: {result_recursive}")
print(f"Iterative Power: {result_iterative}")


def recursive_power(base, exponent):
    """
    Calculate the power of a number using recursion.

    :param base: The base number.
    :param exponent: The exponent.
    :return: The result of base^exponent.
    """
    if exponent == 0:
        return 1
    else:
        return base * recursive_power(base, exponent - 1)

def iterative_power(base, exponent):
    """
    Calculate the power of a number using iteration.

    :param base: The base number.
    :param exponent: The exponent.
    :return: The result of base^exponent.
    """
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result

# Comparison
base_number = 2
exponent_value = 3

# Recursive
result_recursive = recursive_power(base_number, exponent_value)

# Iterative
result_iterative = iterative_power(base_number, exponent_value)

# Display results
print(f"Recursive Power: {result_recursive}")
print(f"Iterative Power: {result_iterative}")


# the same as above but with inputing base annd exponent value

def recursive_power(base, exponent):
    """
    Calculate the power of a number using recursion.

    :param base: The base number.
    :param exponent: The exponent.
    :return: The result of base^exponent.
    """
    if exponent == 0:
        return 1
    else:
        return base * recursive_power(base, exponent - 1)

def iterative_power(base, exponent):
    """
    Calculate the power of a number using iteration.

    :param base: The base number.
    :param exponent: The exponent.
    :return: The result of base^exponent.
    """
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result

# Get user input for base and exponent
base_number = float(input("Enter the base number: "))
exponent_value = int(input("Enter the exponent (a non-negative integer): "))

# Recursive
result_recursive = recursive_power(base_number, exponent_value)

# Iterative
result_iterative = iterative_power(base_number, exponent_value)

# Display results
print(f"Recursive Power: {result_recursive}")
print(f"Iterative Power: {result_iterative}")
