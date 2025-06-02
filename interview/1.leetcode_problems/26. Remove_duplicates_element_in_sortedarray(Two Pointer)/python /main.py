def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    # Pointer 1: Slow pointer, points to the last unique element
    slow = 0

    # Pointer 2: Fast pointer, scans the array
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
