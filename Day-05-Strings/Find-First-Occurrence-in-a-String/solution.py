def str_str(haystack, needle):
    n = len(needle)

    for i in range(len(haystack) - n + 1):
        if haystack[i:i+n] == needle:
            return i

    return -1


# Test Cases
if __name__ == "__main__":
    print(str_str("sadbutsad", "sad"))  # 0
    print(str_str("leetcode", "leeto")) # -1