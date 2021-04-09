# Created by Ellie Le at 4/8/2021

"""
Project problem: P-1.30

Write a Python program that can take a positive integer greater than 2 as input
and write out the number of times one must repeatedly divide this number by 2 before
getting a value less than 2.

"""

def input_postive_integer():
    while True:
        try:
            num = int(input("Enter a number greater than 2: "))
            if num <= 0:
                raise ValueError
                break
            elif num <= 2:
                raise Exception
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer")
        except Exception:
            print("Please enter a number greater than 2")
        return num

def divide_by_2(num):
    count = 0
    while True:
        num = num / 2
        count += 1
        if num < 2:
            break
    return count
    print(count)

divide_by_2(input_postive_integer())

