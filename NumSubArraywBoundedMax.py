def numSubarrayBoundedMax(nums, left, right):
    """
    type: List[int], int, int
    rtype: int
    """
    mid = 0
    low = 0
    result = 0
    
    for num in nums:
        if num > right:
            mid = 0
        else:
            mid += 1
            result += mid
        if num >= left:
            low = 0
        else:
            low += 1
            result -= low
    return result