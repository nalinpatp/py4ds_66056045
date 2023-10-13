"""
Execise 1
"""


def greeting():
    """
    Function to print a greeting message in Thai language.
    """
    # Fix : complete this
    print('สวัสดีชาวลาดกระบัง')


def know_my_name():
    """
    Asks the user for their name and returns it.

    Parameters:
        None
    Returns:
        str: The name entered by the user.
    """
    # Fix : complete this
    name=input('Enter name:')
    return name

def say_hi(name=None):
    """
    Print a greeting message with the given name.

    Args:
        name (str, optional): The name to greet. Defaults to None.
    """
    # Fix : complete this
    sayhi='สวัสดีคุณ' + name
    print(sayhi)

#%%
