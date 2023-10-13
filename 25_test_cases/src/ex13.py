"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    if len(num_list)==0:
        return 0
    else:
        return sum(num_list)


def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    prod=1
    if len(num_list)==0:
        return 1
    else:
        for i in num_list:
            prod=prod*i
        return prod
