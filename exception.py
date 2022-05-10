import math
import os
import random
import re
import sys


#
# Complete the 'Library' function below.
#


def Library(memberfee, installment, book):
    # Write your code here
    try:
        if installment > 3:
            raise ValueError
        amt_per_installment = memberfee / installment

        print("Amount per Installment is  " + str(amt_per_installment))

        if book in ['philosophers stone', 'chamber of secrets', 'prisoner of azkaban', 'goblet of fire',
                    'order of phoenix', 'half blood prince', 'deathly hallows 1', 'deathly hallows 2']:
            print("It is available in this section")
        else:
            raise NameError

    except ValueError:
        print("No such book exists in this section")
    except ZeroDivisionError:
        print("Number of Installments cannot be Zero")
    except NameError:
        print("Maximum Permitted Number of Installements is 3")


if __name__ == '__main__':

    memberfee = int(input())
    installment = int(input())
    book = input()

    try:
        Library(memberfee, installment, book)

    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)