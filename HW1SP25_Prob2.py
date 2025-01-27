# region imports
from Q2Die import rollFairDie, rollUnFairDie
# endregion

# region functions
def rollDice(N=1):
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    total_score = 0
    for _ in range(N):
        total_score += rollFairDie()
    return total_score

def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    total_score = 0
    for _ in range(N):
        total_score += rollUnFairDie()
    return total_score

def main():
    """
    This function rolls nDice fair dice nRolls times and calculates the probabilities for
    each possible score.
    """
    nDice = 2  # Example number of dice
    nMinScore = nDice  # Minimum score (1 per die)
    nMaxScore = 6 * nDice  # Maximum score (6 per die)
    nNumScores = nMaxScore - nMinScore + 1  # Total possible scores
    nTally = [0] * nNumScores  # Tally list initialized to zero
    nRolls = 1000  # Number of rolls

    for _ in range(nRolls):
        score = rollDice(N=nDice)
        nTally[score - nMinScore] += 1  # Increment the tally for the corresponding score

    print("Fair Dice Probabilities:")
    for i in range(nNumScores):
        probability = nTally[i] / nRolls
        print(f"Probability of rolling {i + nMinScore}: {probability:.3f}")

def main2():
    """
    This function rolls 5 unfair dice 1000 times and calculates the probabilities for
    each possible score.
    """
    nDice = 5  # Number of dice
    nMinScore = nDice  # Minimum score (1 per die)
    nMaxScore = 6 * nDice  # Maximum score (6 per die)
    nNumScores = nMaxScore - nMinScore + 1  # Total possible scores
    nTally = [0] * nNumScores  # Tally list initialized to zero
    nRolls = 1000  # Number of rolls

    for _ in range(nRolls):
        score = rollUnFairDice(N=nDice)
        nTally[score - nMinScore] += 1  # Increment the tally for the corresponding score

    print("UnFair Dice Probabilities:")
    for i in range(nNumScores):
        probability = nTally[i] / nRolls
        print(f"Probability of rolling {i + nMinScore}: {probability:.3f}")

# The if statement below is known as: main guarding
if __name__ == "__main__":
    main()
    main2()
