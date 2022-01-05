"""
time complexity: O(n) time
space complexity: O(1) because we are not storing any values other than the
last two numbers calculated
"""


def get_nth_fib(num):
    """
    This is the iterative version of the algorithm. Our solution relies on
    only saving the last two calculations of the fibonacci sequence for quick
    calculation of the sequence.

    :param num: the number we wish to calculate the fibonacci sequence for
    :return: returns calculated fibonacci value
    """

    # the base case of the algorithm
    last_two_values = [0, 1]
    # counter for the algorithm starting at 3 (since base cases controlled for)
    counter = 3

    # while loop that iterates for the fibonacci sequence
    while counter <= num:
        # next_fib_sequence is equal to the summation of base cases
        next_fib_sequence = last_two_values[0] + last_two_values[1]

        # next_fib_sequence[0] takes on the value of [1]
        last_two_values[0] = last_two_values[1]

        # next_fib_sequence[1] takes on the value of [n]
        last_two_values[1] = next_fib_sequence

        # increase the counter for the while loop to continue
        counter += 1

    # control for the base case of being at [1}
    return last_two_values[1] if num > 1 else last_two_values[0]


print(get_nth_fib(5))
