def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res


# Test cases
if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))  # [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3]))  # [0,0,9,0,0]