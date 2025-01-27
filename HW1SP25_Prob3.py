# region imports
import random as rnd
# endregion

# region functions
def between(num, low, high, inclusivelow=True, inclusivehigh=True):
    """
    Determine if a number is within a specified range.

    This function checks whether a given number lies between a lower and upper limit, with options to include or
    exclude the boundary values.

    :param num: float, the number to check.
    :param low: float, the lower bound of the range.
    :param high: float, the upper bound of the range.
    :param inclusivelow: bool, whether to include the lower bound in the range.
    :param inclusivehigh: bool, whether to include the upper bound in the range.
    :return: bool, True if the number is within the range, False otherwise.
    """
    if inclusivelow and inclusivehigh:
        return low <= num <= high
    elif inclusivelow:
        return low <= num < high
    elif inclusivehigh:
        return low < num <= high
    else:
        return low < num < high

def main():
    """
    Generate and analyze normally distributed data.

    This function generates an array of random numbers from a normal distribution with a specified mean and
    standard deviation. It calculates the percentage of values within 1, 2, and 3 standard deviations of the mean,
    verifying the data follows the properties of a normal distribution.

    :return: None
    """
    N = 1000  # size of array I want
    arr = []  # array for storing the numbers
    mean = 50  # the mean I want
    stdev = 10  # the standard deviation

    bin1 = 0  # normal dist should contain 68% within +/-1stdev
    bin2 = 0  # normal dist should contain 95.5% within +/-2stdev
    bin3 = 0  # normal dist should contain 99.7% within +/-3stdev

    # find edges of the limits for the various bins
    bin1low = mean - stdev
    bin1high = mean + stdev

    bin2low = mean - 2 * stdev
    bin2high = mean + 2 * stdev

    bin3low = mean - 3 * stdev
    bin3high = mean + 3 * stdev

    for i in range(N):  # this loop generates the numbers
        num = rnd.normalvariate(mean, stdev)
        arr.append(num)
        # this checks which bin(s) the current number is in.
        if between(num, bin1low, bin1high):
            bin1 += 1
        if between(num, bin2low, bin2high):
            bin2 += 1
        if between(num, bin3low, bin3high):
            bin3 += 1

    #print(arr)  # If I want to see the actual array, uncomment this.
    print("{:.1f}% of data within +/-1 StDev of mean.".format(100 * bin1 / N))
    print("{:.1f}% of data within +/-2 StDev of mean.".format(100 * bin2 / N))
    print("{:.1f}% of data within +/-3 StDev of mean.".format(100 * bin3 / N))
# endregion

if __name__ == "__main__":
    main()  # calls the function main
