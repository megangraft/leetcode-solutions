def singleNumber(nums):
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    nums.append(0)
    i, j = 0, 1
    while nums[i] == nums[j]:
        i, j = i + 2, j + 2
    return nums[i]