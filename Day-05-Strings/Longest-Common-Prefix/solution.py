def longest_common_prefix(strs):
    prefix = strs[0]

    for string in strs[1:]:

        while string.find(prefix) != 0:
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


# Test Cases
if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))  # fl
    print(longest_common_prefix(["dog","racecar","car"]))     # ""