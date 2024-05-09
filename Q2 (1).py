def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left

# Test cases
nums1, target1 = [1,3,5,6], 5
nums2, target2 = [1,3,5,6], 2
nums3, target3 = [1,3,5,6], 7

print(searchInsert(nums1, target1))  
print(searchInsert(nums2, target2))  
print(searchInsert(nums3, target3))  
