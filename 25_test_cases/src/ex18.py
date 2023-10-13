"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(cups, price):
    free=0
    temp=cups
    if cups<=8:
        return cups*price
    else:
        while(temp>8):
            temp=temp-8
            free=free+1
        return (cups-free)*price


