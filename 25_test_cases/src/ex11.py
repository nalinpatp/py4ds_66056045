"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    temp=tsec
    hr=0
    min=0
    sec=0
    word=''
    if tsec==0:
        return '0s'
    while(temp>=3600):
        temp=temp-3600
        hr=hr+1
    while(temp>=60):
        temp=temp-60
        min=min+1
    sec=temp
    if hr!=0:
        word=word+str(hr)+'h'
    if min!=0:
        if word!='':
            word=word+' '+str(min)+'m'
        else:
            word=word+str(min)+'m'
    if sec!=0:
        if word!='':
            word=word+' '+str(sec)+'s'
        else:
            word=word+str(sec)+'s'
    return word

