def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare the characters in a case-insensitive manner
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Test cases
print(isPalindrome('Madam'))                             # Output: True
print(isPalindrome('sir'))                               # Output: False
print(isPalindrome('A man, a plan, a canal: Panama'))    # Output: True
print(isPalindrome('race a car'))                        # Output: False
print(isPalindrome('No lemon, no melon'))                # Output: True
