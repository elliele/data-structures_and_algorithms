# Created by Ellie Le at 4/14/2021


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
