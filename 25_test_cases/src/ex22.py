"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(p1, p2):
    """
    Check the result of a rock-paper-scissors game between two players.

    Parameters:
        p1 (str): The choice of player one. It can be 'rock', 'paper', or 'scissor'.
        p2 (str): The choice of player two. It can be 'rock', 'paper', or 'scissor'.

    Returns:
        str: The result of the game. It can be 'player one', 'player two', or 'tie'.
    """
    # TODO : complete this
    if p1==p2:
        return 'tie'
    elif p1=='rock' and p2=='paper':
        return 'player two'
    elif p1=='rock' and p2=='scissors':
        return 'player one'
    elif p1=='paper' and p2=='scissors':
        return 'player two'
    elif p1=='paper' and p2=='rock':
        return 'player one'
    elif p1=='scissors' and p2=='rock':
        return 'player two'
    elif p1=='scissors' and p2=='paper':
        return 'player one'
    else:
        print('Invalid Input')
