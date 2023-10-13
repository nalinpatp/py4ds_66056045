"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    position=(len(num_list)+1)/2
    if len(num_list)==0:
        return None
    else:
        sorted(num_list)
        if len(num_list)%2!=0:
            Med=num_list[position-1]
        else:
            Med=(num_list[(len(num_list)+1)/2+0.5]+num_list[(len(num_list)+1)/2+0.5])/2
        return Med

