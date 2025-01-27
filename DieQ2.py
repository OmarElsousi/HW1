# region imports
from Die import rollFairDie as rfd
from random import random
# endregion

# region function declarations
def rollFairDie():
    """
    This function simulates rolling a fair die such that the probability of each integer is 1/6.
    Each roll is independent of the past or future rolls.
    :return: an integer between 1 and 6 inclusive
    """
    x = random()  # Produce a floating point number between 0.0 and 1.0
    if x <= 1/6:
        return 1
    elif x <= 2/6:
        return 2
    elif x <= 3/6:
        return 3
    elif x <= 4/6:
        return 4
    elif x <= 5/6:
        return 5
    else:
        return 6

def rollUnFairDie():
    """
    This function simulates rolling an unfair die such that the probability of rolling a 1 is 0.2, with all other
    integers having equal probability. Now, the probability of numbers 2-6 should be 0.8/5.
    :return: an integer between 1 and 6 inclusive
    """
    x = random()
    if x <= 0.2:
        return 1
    elif x <= 0.2 + 0.8/5:
        return 2
    elif x <= 0.2 + 2*(0.8/5):
        return 3
    elif x <= 0.2 + 3*(0.8/5):
        return 4
    elif x <= 0.2 + 4*(0.8/5):
        return 5
    else:
        return 6

def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6  # create a list with 6 elements/items initialized to 0's
    n = 1000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start

    # print the result
    print("After rolling the die 1000 times:")
    for i, count in enumerate(scores):
        print(f"Probability of rolling a {i + 1}: {count / n:.4f}")

def main2():
    """
    This function rolls a fair die 10000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6  # create a list with 6 elements/items initialized to 0's
    n = 10000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rollFairDie()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start

    # print the result
    for i, count in enumerate(scores):
        print(f"Score {i + 1}: Count = {count}, Probability = {count / n:.2f}")

def main3():
    """
    This function rolls an unfair die 10000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0] * 6  # create a list with 6 elements/items initialized to 0's
    n = 10000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rollUnFairDie()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start

    # print the result
    for i, count in enumerate(scores):
        print(f"Score {i + 1}: Count = {count}, Probability = {count / n:.2f}")

# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()
    main3()
