from itertools import combinations
import statistics


def mean_median_diff(subset):
    if len(subset) == 0:
        return float('-inf')
    mean = sum(subset) / len(subset)
    median = statistics.median(subset)
    return mean - median


def max_val(n, a):
    max_value = float('-inf')

    for i in range(1, n + 1):
        for comb in combinations(a, i):
            max_value = max(max_value, mean_median_diff(comb))

    return max_value


# Input from the user
n = int(input("Enter the number of elements in the array: "))
a = list(map(int, input("Enter the elements of the array separated by space: ").split()))

# Output the result
result = max_val(n, a)
print(f"The maximum value of Mean(S) - Median(S) for all subsets is: {result}")
