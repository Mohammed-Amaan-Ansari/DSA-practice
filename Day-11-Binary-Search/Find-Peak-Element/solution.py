def find_peak_element(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    print(find_peak_element([1,2,3,1]))  # 2
    print(find_peak_element([1,2,1,3,5,6,4]))  # 1 or 5