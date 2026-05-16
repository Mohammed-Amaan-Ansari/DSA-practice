import math

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    result = right

    while left <= right:
        mid = (left + right) // 2

        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == "__main__":
    print(min_eating_speed([3,6,7,11], 8))  # 4
    print(min_eating_speed([30,11,23,4,20], 5))  # 30