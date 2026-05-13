def next_greater_element(nums1, nums2):
    stack = []
    mapping = {}

    for num in nums2:
        while stack and num > stack[-1]:
            mapping[stack.pop()] = num

        stack.append(num)

    while stack:
        mapping[stack.pop()] = -1

    return [mapping[num] for num in nums1]


if __name__ == "__main__":
    print(next_greater_element([4,1,2], [1,3,4,2]))