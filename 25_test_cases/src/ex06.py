"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # Fix : complete this
    int(num)
    tempnum=num
    while tempnum>=100:
        tempnum=tempnum%100
    if tempnum >= 0:
        if tempnum==1:
            prefix='st'
        elif tempnum==2:
            prefix='nd'
        elif tempnum==3:
            prefix='rd'
        else:
            prefix='th'
        return str(num)+prefix
    else:
        print('Your parameter is negative')


