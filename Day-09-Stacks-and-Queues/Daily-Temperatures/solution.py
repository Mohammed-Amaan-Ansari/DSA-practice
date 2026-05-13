def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index

        stack.append(i)

    return result


if __name__ == "__main__":
    print(daily_temperatures([73,74,75,71,69,72,76,73]))