def find_duplicate(nums):
    if not nums:
        return False

    for index, number in enumerate(nums):
        for candidate in nums[index + 1:]:
            if number == candidate and number > 0:
                return number

    return False
