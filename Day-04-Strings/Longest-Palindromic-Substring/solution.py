def longest_palindrome(s):

    result = ""
    max_length = 0

    for i in range(len(s)):

        # Odd length palindrome
        left = right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:

            if (right - left + 1) > max_length:
                result = s[left:right + 1]
                max_length = right - left + 1

            left -= 1
            right += 1

        # Even length palindrome
        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:

            if (right - left + 1) > max_length:
                result = s[left:right + 1]
                max_length = right - left + 1

            left -= 1
            right += 1

    return result


# Test Cases
if __name__ == "__main__":
    print(longest_palindrome("babad"))  # bab
    print(longest_palindrome("cbbd"))   # bb