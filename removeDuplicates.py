def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 1
    while i < len(nums):  # Must use while since array size changes
        if nums[i] == nums[i-1]:  # Compare with previous element
            nums.pop(i)  # Remove current element if duplicate
        else:
            i += 1  # Only increment if no duplicate found
    
    return len(nums)

# Test cases
nums = [1, 1, 2]
removeDuplicates(nums)
print(nums)  # [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
removeDuplicates(nums)
print(nums)  # [0, 1, 2, 3, 4]