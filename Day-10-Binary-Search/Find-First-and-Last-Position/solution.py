def search_range(nums, target):

    def find_bound(left_bound):
        left = 0
        right = len(nums) - 1
        bound = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                bound = mid

                if left_bound:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return bound

    return [find_bound(True), find_bound(False)]


if __name__ == "__main__":
    print(search_range([5,7,7,8,8,10], 8))  # [3,4]