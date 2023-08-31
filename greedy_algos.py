#BASIC - MICE IN HOLES

# Returns minimum time required to place mice in holes using the Greedy approach. We can put every mouse
# to its nearest hole to minimize the time. This can be done by sorting the positions of mice and holes.

def assignHole(mice, holes):

    # Base - num of mice and holes should be the same
    if len(mice) != len(holes):
        return "Number of mice and holes not the same"

    # Sort first
    mice.sort()
    holes.sort()

    # Finding max difference between ith mice and hole
    max_diff = 0

    for i in range(len(mice)):
        if max_diff < abs(mice[i] - holes[i]):
            max_diff = abs(mice[i] - holes[i])

    return max_diff


mice = [4, -4, 2]

# Hole positions
holes = [4, 0, 5]

# The required answer is returned from the function
min_time = assignHole(mice, holes)

print("The last mouse gets into the hole in time:", min_time)

################################################################

# Advanced: Fractional Knapsack



weight = [30, 50, 12, 70, 40]
value = [150, 100, 90, 140, 120]
capacity = 150

def fractional_knapsack(value, weight, capacity):

    items = list(range(len(value)))
    print(items)
    ratio = [v//w for v, w in zip(value, weight)]
    print(ratio)
    srt_ratios = sorted(ratio, reverse=True)
    print(srt_ratios)
    items.sort(key=lambda i: ratio[i], reverse=True)
    print(items)

    max_value = 0
    fractions = [0] * len(value)
    print(fractions)
    for i in items:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
            print(max_value)
        else:
            fractions[i] = capacity // weight[i]
            max_value += value[i] * capacity // weight[i]

    return max_value

print(fractional_knapsack(value, weight, capacity))


########################################################################

# MINDBREAKER: Egyptian Fractions

# Python3 program to print an Egyptian fraction in Egyptian Form using Greedy Algorithm

import math
import fractions
import functools

def main():
    f = fractions.Fraction(3, 4)
    e = to_egyptian_fractions(f)
    print(*e, sep=' + ')
    f = fractions.Fraction(6, 7)
    e = to_egyptian_fractions(f)
    print(*e, sep=' + ')
    f = fractions.Fraction(7654, 321)
    e = to_egyptian_fractions(f)
    print(*e, sep=' + ')


def validate(function):
    @functools.wraps(function)
    def wrapper(fraction):
        total = fractions.Fraction(0)
        for egyptian in function(fraction):
            if 1 not in {egyptian.numerator, egyptian.denominator}:
                raise AssertionError('function has failed validation')
            yield egyptian
            total += egyptian
        if total != fraction:
            raise AssertionError('function has failed validation')
    return wrapper


@validate
def to_egyptian_fractions(fraction):
    quotient = math.floor(fraction.numerator / fraction.denominator)
    if quotient:
        egyptian = fractions.Fraction(quotient, 1)
        yield egyptian
        fraction -= egyptian
    while fraction:
        quotient = math.ceil(fraction.denominator / fraction.numerator)
        egyptian = fractions.Fraction(1, quotient)
        yield egyptian
        fraction -= egyptian


# if __name__ == '__main__':
#     main()
