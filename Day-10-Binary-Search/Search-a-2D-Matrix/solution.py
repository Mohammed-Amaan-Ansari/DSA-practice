def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // cols
        col = mid % cols

        value = matrix[row][col]

        if value == target:
            return True

        elif value < target:
            left = mid + 1

        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]

    print(search_matrix(matrix, 3))   # True
    print(search_matrix(matrix, 13))  # False