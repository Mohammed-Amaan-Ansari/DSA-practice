def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


# Test cases
if __name__ == "__main__":
    print(contains_duplicate([1,2,3,1]))  # True
    print(contains_duplicate([1,2,3,4]))  # False