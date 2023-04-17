from collections import Counter


def find_duplicate(nums):
    if not nums:
        return False

    repeated_number = Counter(nums).most_common()[0]
    if not repeated_number[1] <= 1 and repeated_number[0] > 0:
        return repeated_number[0]

    return False
