# region imports
from random import random
from collections import Counter


# endregion

# region functions
def rollFairDie():
    """
    This function simulates rolling a fair die such that the probability of each integer is 1/6.
    :return: an integer between 1 and 6 inclusive
    """
    x = random()  # should be a floating point number between 0.0 and 1.0
    if x <= 1 / 6:
        return 1
    elif x <= 2 / 6:
        return 2
    elif x <= 3 / 6:
        return 3
    elif x <= 4 / 6:
        return 4
    elif x <= 5 / 6:
        return 5
    else:
        return 6


def rollUnFairDie():
    """
    This function simulates rolling an unfair die such that the probability of rolling a 1 is 0.2,
    with all other integers having equal probability. Now, the probability of numbers 2-6 should be 0.8/5.
    :return: an integer between 1 and 6 inclusive
    """
    x = random()
    if x <= 0.2:  # Probability of 1 is 0.2
        return 1
    elif x <= 0.2 + 0.8 / 5:  # Probability of 2 is 0.16
        return 2
    elif x <= 0.2 + 2 * (0.8 / 5):  # Probability of 3 is 0.16
        return 3
    elif x <= 0.2 + 3 * (0.8 / 5):  # Probability of 4 is 0.16
        return 4
    elif x <= 0.2 + 4 * (0.8 / 5):  # Probability of 5 is 0.16
        return 5
    else:  # Probability of 6 is 0.16
        return 6


def main3():
    """
    Simulates rolling an unfair die 10,000 times and outputs the observed probabilities for each number.
    """
    # Number of rolls
    num_rolls = 10000

    # Roll the unfair die 10,000 times
    results = [rollUnFairDie() for _ in range(num_rolls)]

    # Count the occurrences of each result
    counts = Counter(results)

    # Print the observed probabilities
    print(f"Unfair die roll results ({num_rolls} trials):")
    for number in range(1, 7):
        observed_probability = counts[number] / num_rolls
        print(f"Number {number}: {observed_probability:.2%} ({counts[number]} occurrences)")


# endregion

# The if statement below is known as: main guarding
if __name__ == "__main__":
    # Test rolling the fair and unfair dice
    print("Fair die roll:", rollFairDie())
    print("Unfair die roll:", rollUnFairDie())
    main3()
