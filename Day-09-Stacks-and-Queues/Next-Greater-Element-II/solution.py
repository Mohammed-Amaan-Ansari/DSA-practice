def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        while stack and nums[i % n] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i % n]

        if i < n:
            stack.append(i)

    return result


if __name__ == "__main__":
    print(next_greater_elements([1,2,1]))