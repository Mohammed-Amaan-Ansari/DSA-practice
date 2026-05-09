def repeated_substring_pattern(s):
    doubled = s + s
    return s in doubled[1:-1]


# Test Cases
if __name__ == "__main__":
    print(repeated_substring_pattern("abab"))  # True
    print(repeated_substring_pattern("aba"))   # False