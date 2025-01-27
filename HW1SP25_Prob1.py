# region imports
from Die import rollFairDie, rollUnFairDie  # Assuming rollFairDie() and rollUnFairDie() are defined in Die module
from collections import Counter
# endregion

# region functions
def main():
    """
    Simulates rolling a fair die 1,000 times, computes the fraction of rolls
    that yield each number, and prints the observed probabilities to the CLI.
    """
    num_rolls = 1000
    results = [rollFairDie() for _ in range(num_rolls)]
    counts = Counter(results)

    print(f"Results after {num_rolls} rolls of a fair die:")
    for number in range(1, 7):
        observed_probability = counts[number] / num_rolls
        print(f"Number {number}: {observed_probability:.2%} ({counts[number]} occurrences)")


def main2():
    """
    Simulates rolling a fair die 10,000 times, computes the fraction of rolls
    that yield each number, and prints the observed probabilities to the CLI.
    """
    num_rolls = 10000
    results = [rollFairDie() for _ in range(num_rolls)]
    counts = Counter(results)

    print(f"\nResults after {num_rolls} rolls of a fair die:")
    for number in range(1, 7):
        observed_probability = counts[number] / num_rolls
        print(f"Number {number}: {observed_probability:.2%} ({counts[number]} occurrences)")

    # Theoretical probability
    theoretical_probability = 1 / 6
    print("\nTheoretical probabilities:")
    for number in range(1, 7):
        print(f"Number {number}: {theoretical_probability:.2%}")

    print("\nComparison:")
    for number in range(1, 7):
        observed_probability = counts[number] / num_rolls
        difference = observed_probability - theoretical_probability
        print(f"Number {number}: Observed = {observed_probability:.2%}, "
              f"Theoretical = {theoretical_probability:.2%}, "
              f"Difference = {difference:.2%}")


def main3():
    """
    Simulates rolling an unfair die 10,000 times, computes the fraction of rolls
    that yield each number, and prints the observed probabilities to the CLI.
    """
    num_rolls = 10000
    results = [rollUnFairDie() for _ in range(num_rolls)]
    counts = Counter(results)

    print(f"\nResults after {num_rolls} rolls of an unfair die:")
    for number in range(1, 7):
        observed_probability = counts[number] / num_rolls
        print(f"Number {number}: {observed_probability:.2%} ({counts[number]} occurrences)")

    # Theoretical probabilities for the unfair die
    theoretical_probabilities = {1: 0.2, 2: 0.16, 3: 0.16, 4: 0.16, 5: 0.16, 6: 0.16}
    print("\nTheoretical probabilities for unfair die:")
    for number in range(1, 7):
        print(f"Number {number}: {theoretical_probabilities[number]:.2%}")

    print("\nComparison:")
    for number in range(1, 7):
        observed_probability = counts[number] / num_rolls
        difference = observed_probability - theoretical_probabilities[number]
        print(f"Number {number}: Observed = {observed_probability:.2%}, "
              f"Theoretical = {theoretical_probabilities[number]:.2%}, "
              f"Difference = {difference:.2%}")

# endregion

# The if statement below is known as: main guarding
if __name__ == "__main__":
    main()
    main2()
    main3()
