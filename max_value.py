#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: May 18, 2025

# Max number in array program in python

import random


def get_max_number(array):

    # Initialize max
    max = 0

    # Find max number by comparing last highest
    for number in array:
        if number > max:
            max = number

    # Return max
    return max


def main():

    # Initialize array
    array = []

    # Add random numbers 10 times to the array
    for counter in range(10):

        # Append and display random number
        random_num = random.randint(1, 99)
        print("Adding {} to the array!".format(random_num))
        array.append(random_num)

    # Set max to function call and display
    highest_num = get_max_number(array)
    print("The highest number in the array was", highest_num, "!")


if __name__ == "__main__":
    main()
